# utils.py

""" 
OAIUtils : A set of utility functions that handle requests and format responses for OAI provider. 

http://www.openarchives.org/OAI/openarchivesprotocol.html
"""
import json

from django.utils import timezone, dateparse

from oaipmh.client import BaseClient, Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader

# Sickle implementation: https://sickle.readthedocs.io/en/latest/
import string, urllib
from collections import defaultdict

from sickle import Sickle
from sickle.utils import xml_to_dict, get_namespace
from sickle.models import Record, Header

from .models import Collection, Record as LocalRecord, MetadataElement



def filter_existing_collections(collections):
    """ Returns a list of tuples containing collections not present in local db."""
    collections_filtered = []
    cols = Collection.objects.all()
    for i in collections:
        if not cols.filter(identifier=i[0]):
            collections_filtered.append(i)
    return collections_filtered

def dim_xml_to_dict(tree):
    fields = defaultdict(list)
    for tag in tree.getchildren():
        f = tag.get('element')
        q = tag.get('qualifier')
        if q: f += '.' + q
        fields[f].append(tag.text)    
    return dict(fields)

def get_bitstream_url(collection, record):
    """ Harvests an href pointing to the bitstream urls for the record in repository.
    E.g., https://scholarspace.manoa.hawaii.edu/bitstream/10125/25006/1/editor.pdf
    """
    bitstreams = {'bitstream': None, 'bitstream_txt': None}
    try:
        sickle = Sickle(collection.community.repository.base_url)        
        sickle.class_mapping['GetRecord'] = LltRecordBitstream
        record = sickle.GetRecord(metadataPrefix='ore', identifier=record.header.identifier)
        
        record.metadata['bitstream'][0].replace('+', '%20')
        bitstreams['bitstream'] = record.metadata['bitstream'][0]
        record.metadata['bitstream_txt'][0].replace('+', '%20')
        bitstreams['bitstream_txt'] = record.metadata['bitstream_txt'][0]

    
    except Exception as e:
        print e, 'Unable to construct bitstream url.'
    
    return bitstreams

def batch_harvest_articles(collection_obj):
    oai = OAIUtils()
    records = oai.harvest_oai_collection_records_sickle(collection_obj)

    for record in records:
        # Read Header
        if not record.header.deleted:
            repo_date = dateparse.parse_datetime(record.header.datestamp)
            try:
                record_obj = LocalRecord.objects.get(identifier=record.header.identifier)            
                record_obj.remove_data()
                record_obj.hdr_datestamp = repo_date

            except Exception as e:
                print 'Creating new Record object.', record.header.identifier
                record_obj = LocalRecord()
                record_obj.identifier = record.header.identifier
                record_obj.hdr_datestamp = repo_date
                record_obj.hdr_setSpec = collection_obj
            
            record_obj.save()

            # Read Metadata
            dataelements = record.metadata
            for key in dataelements:
                element = MetadataElement()
                element.record = record_obj
                element.element_type = key
                data = dataelements[key]
                element.element_data = json.dumps(data)
                element.save()

            #  Add in bitstream urls
            bitstreams = get_bitstream_url(collection_obj, record)
            element = MetadataElement()
            element.record = record_obj
            element.element_type = 'bitstream'
            element.element_data = json.dumps([bitstreams['bitstream']])
            element.save()

            element = MetadataElement()
            element.record = record_obj
            element.element_type = 'bitstream_txt'
            element.element_data = json.dumps([bitstreams['bitstream_txt']])
            element.save()
        else:
            try:
                record_obj = LocalRecord.objects.get(identifier=record.header.identifier)
                record_obj.delete()     
            except:
                pass

def batch_harvest_issues(community_obj):
    oai = OAIUtils()
    issues = oai.list_oai_collections(community_obj)
    for i in issues:
        col = Collection(identifier=i[0], name=i[1], community=community_obj)
        try:
            col.save()
        except Exception as e:
            print 'collection already added to db', e
            col = Collection.objects.get(identifier=i[0])
        
        batch_harvest_articles(col)


class LltRecord(Record):
    """ XML Record handler override for dim metadata format. """    
    def __init__(self, record_element, strip_ns=True):
        super(LltRecord, self).__init__(record_element, strip_ns=strip_ns)
        self.header = Header(self.xml.find('.//' + self._oai_namespace + 'header'))
        print self.header.identifier, self.header.deleted
        if not self.header.deleted:
            tree = self.xml.find('.//' + self._oai_namespace + 'metadata').getchildren()[0]
            self.metadata = dim_xml_to_dict(tree)


class LltRecordBitstream(Record):
    """ XML Record handler override for ore metadata format. Used to retrieve bitstream url for a record."""    
    def __init__(self, record_element, strip_ns=True):
        super(LltRecordBitstream, self).__init__(record_element, strip_ns=strip_ns)
        self._oai_namespace = get_namespace(self.xml)
        rdfnamespace = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'

        tree = self.xml.find('.//' + self._oai_namespace + 'metadata').getchildren()[0]
        bitstream_urls = tree.findall('.//'+rdfnamespace+'Description')

        # for debugging in shell
        self.bits = bitstream_urls
        
        #  clear the metadata. we're only interested in fishing out the bitstream info.
        self.metadata.clear()
        
        for i in bitstream_urls:
            bittype = i.find(rdfnamespace+'type').get(rdfnamespace+'resource')

            if bittype != 'http://www.dspace.org/objectModel/DSpaceItem':
                biturl = i.get(rdfnamespace+'about')
                if biturl[-3:] == 'pdf':
                    self.metadata['bitstream'] = [biturl]
                else:
                    self.metadata['bitstream_txt'] = [biturl]
        
        # for i in bitstream_urls:
        #     print i
        #     # if i.get('rel') == 'http://www.openarchives.org/ore/terms/aggregates':
            #     self.metadata = {'bitstream': [i.get('href')]}


class OAIUtils(object):
    """ Provides an api for interacting with and harvesting from the 
    OAI repository. Utilizes the sickle module as a wrapper for requests.
    """

    def __init__(self):
        self.repositories = []
        self.communities = []
        self.collections = []

    def list_oai_community_sets(self, repository):
        """ Contructs list of tuples of communities (a grouping concept in OAI) 
        for the given repository.
        Utilizes OAI-PMH verb: ListSets
        """
        try:
            sickle = Sickle(repository.base_url)
            sets = sickle.ListSets()
        except:
            return

        """ Filter set list to build list of community sets """
        for i in sets:
            """ Build community tuples (id, human readable name) """
            if i.setSpec[:3] == 'com':
                set_data = (i.setSpec, i.setName)
                self.communities.append(set_data)

        self.communities = sorted(self.communities, key=lambda i: i[1])

    def list_oai_collections(self, community):
        """ Constructs list of tuples of collections (a seconday grouping concept
        in OAI) "owned" by the given community.
        
        Utilizes OAI-PMH verbs: ListIdentifiers and ListSets
        """
        sickle = Sickle(community.repository.base_url)
        # Retrieve collections associated with community parameter
        record_headers = sickle.ListIdentifiers(metadataPrefix='oai_dc', set=community.identifier)
        
        # Filter record headers to build collection map from the community
        community_collections = {}  
        for i in record_headers:
            # Iterate over associated sets looking for collections 
            for j in i.setSpecs:     
                if j[:3] == 'col':
                    community_collections[j] = None  # register id in map

        # Map names to ids in collection map {setSpec: setName}         
        for i in sickle.ListSets():
            if i.setSpec in community_collections:
                community_collections[i.setSpec] = i.setName

        # Convert map to list of tuples
        self.collections = community_collections.items()

        # Sort collections by name
        self.collections = sorted(self.collections, key=lambda i: i[1])
        return self.collections

    def harvest_oai_collection_records_sickle(self, collection):
        sickle = Sickle(collection.community.repository.base_url)
        sickle.class_mapping['ListRecords'] = LltRecord
        sickle.class_mapping['GetRecord'] = LltRecord
        records = sickle.ListRecords(metadataPrefix='dim', ignore_deleted=True, set=collection.identifier)
        return records
