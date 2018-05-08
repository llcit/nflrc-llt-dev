import json
from operator import itemgetter
from collections import Counter
import urllib
import urllib2

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.db.models import Q
from django.contrib import messages
from django.conf import settings

from braces.views import LoginRequiredMixin
from haystack.generic_views import SearchView

from oaiharvests.models import Community, Collection, Record, MetadataElement
from .models import StoryPage, Subscriber
from .mixins import RecordSearchMixin
from .forms import CreateSubscriberForm


class HomeView(TemplateView):
    template_name = 'home.html'
    queryset = None

    def get(self, request, *args, **kwargs):
        return redirect('page_view', pk=15)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        journal = Community.objects.all()[0]
        context['keywords'] =  journal.aggregate_keywords()
        context['volumes'] = journal.list_collections_by_volume()
        context['latest'] = Collection.objects.all().order_by('-name')[0]
        context['toc'] = context['latest'].list_toc_by_page()
        # context['latest'] = [(vol, vol.list_records()) for vol in Collection.objects.all().order_by('-name')][0]
        return context


class PreviousIssuesView(TemplateView):
    template_name = 'previous_issues.html'

    def get_context_data(self, **kwargs):
        context = super(PreviousIssuesView, self).get_context_data(**kwargs)
        journal = Community.objects.all()[0]
        context['volumes'] = journal.list_collections_by_volume()
        context['latest'] = [(vol, vol.list_records()) for vol in Collection.objects.all().order_by('-name')][0]
        context['curr_page'] = 'previous_issues'
        return context


class CommunityView(DetailView):
    model = Community
    template_name = 'community_view.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityView, self).get_context_data(**kwargs)
        context['collections'] = self.get_object().list_collections()
        return context


class CollectionListView(ListView):
    model = Collection
    template_name = 'collection_list.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionListView, self).get_context_data(**kwargs)
        return context


class CollectionView(DetailView):
    model = Collection
    template_name = 'collection_view.html'
    queryset = None

    def get_context_data(self, **kwargs):
        context = super(CollectionView, self).get_context_data(**kwargs)
        context['toc'] = self.get_object().list_toc_by_page()
        context['size'] = len(context['toc'])
        return context


class ItemView(DetailView):
    model = Record
    template_name = 'item_view.html'

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context['item_data'] = self.get_object().as_display_dict()
        bitstream = context['item_data']['bitstream'][0]
        context['pdf_filename'] = bitstream[bitstream.rfind('/')+1:]
        return context


class ItemViewFull(DetailView):
    model = Record
    template_name = 'item_view_full.html'

    def get_context_data(self, **kwargs):
        context = super(ItemViewFull, self).get_context_data(**kwargs)
        context['item_data'] = self.get_object().as_dict()
        return context


class PageView(DetailView):
    model = StoryPage
    template_name = 'page_view.html'
    context_object_name = 'page'

    def get(self, request, *args, **kwargs):
        if self.get_object().private:
            # will redirect to login required view
            return redirect('staff_page_view', item=self.get_object().id)
        return super(PageView, self).get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(PageView, self).get_context_data(*args, **kwargs)
        context['admin_edit'] = reverse('admin:lltsite_storypage_change', args=(self.get_object().id,))
        context['curr_page'] = self.get_object().id
        return context


class PageViewPrivate(LoginRequiredMixin, DetailView):
    model = StoryPage
    template_name = 'page_view.html'
    context_object_name = 'page'

    def get_context_data(self, *args, **kwargs):
        context = super(PageViewPrivate, self).get_context_data(*args, **kwargs)
        context['admin_edit'] = reverse('admin:lltsite_storypage_change', args=(self.get_object().id,))
        context['curr_page'] = self.get_object().id
        return context


class SearchHaystackView(SearchView):
    def get_context_data(self, *args, **kwargs):
        context = super(SearchHaystackView, self).get_context_data(*args, **kwargs)

        keylist = ['Assessment/Testing','Behavior-tracking Technology','Blended/Hybrid Learning and Teaching','Code Switching','Collaborative Learning','Computer-Mediated Communication','Concordancing','Corpus','Culture','Data-driven Learning','Digital Literacies','Discourse Analysis','Distance/Open Learning and Teaching','Eye Tracking','Feedback','Game-based Learning and Teaching','Grammar','Human-Computer Interaction','Indigenous Languages','Instructional Context','Instructional Design','Language for Special Purposes','Language Learning Strategies','Language Maintenance','Language Teaching Methodology','Learner Attitudes','Learner Autonomy','Learner Identity','Less Commonly Taught Languages','Listening','Meta Analysis','Mobile Learning','MOOCs','Multiliteracies','Natural Language Processing','Open Educational Resources','Pragmatics','Pronunciation','Reading','Research Methods','Social Context','Sociocultural Theory','Social Networking','Speaking','Speech Recognition','Speech Synthesis','Task-based Learning and Teaching','Teacher Education','Telecollaboration','Ubiquitous Learning and Teaching','Virtual Environments','Vocabulary','Writing']

        cols_length = len(keylist) / 3
        keytable = []
        for i in range(0, len(keylist), cols_length):
            keytable.append(keylist[i:i+cols_length])

        authorlist = []
        for i in MetadataElement.objects.filter(element_type='contributor.author'):
            for j in json.loads(i.element_data):                
                # swap the first and last so last appears after first.
                n = j.split(',')
                try:
                    authorlist.append((n[1].strip(), n[0].strip()))
                except:
                    pass
        
        authorlist = set(authorlist)
        authorlist = sorted(authorlist, key=lambda author: author[1].lower())

        # will create n sets of authors to be rendered in columns
        # cols_length = len(authorlist) / 6
        # authortable = []
        # for i in range(0, len(authorlist), cols_length):
        #     authortable.append(authorlist[i:i+cols_length])

        context['authortable'] = authorlist # using flat list for now. authortable an option if needed.
        context['keytable'] = keytable
        return context


class KeywordBrowseView(TemplateView):
    template_name = 'page_keyword_browse.html'

    def get_context_data(self, **kwargs):
        context = super(KeywordBrowseView, self).get_context_data(**kwargs)
        
        keylist = ['Assessment/Testing','Behavior-tracking Technology','Blended/Hybrid Learning and Teaching','Code Switching','Collaborative Learning','Computer-Mediated Communication','Concordancing','Corpus','Culture','Data-driven Learning','Digital Literacies','Discourse Analysis','Distance/Open Learning and Teaching','Eye Tracking','Feedback','Game-based Learning and Teaching','Grammar','Human-Computer Interaction','Indigenous Languages','Instructional Context','Instructional Design','Language for Special Purposes','Language Learning Strategies','Language Maintenance','Language Teaching Methodology','Learner Attitudes','Learner Autonomy','Learner Identity','Less Commonly Taught Languages','Listening','Meta Analysis','Mobile Learning','MOOCs','Multiliteracies','Natural Language Processing','Open Educational Resources','Pragmatics','Pronunciation','Reading','Research Methods','Social Context','Sociocultural Theory','Social Networking','Speaking','Speech Recognition','Speech Synthesis','Task-based Learning and Teaching','Teacher Education','Telecollaboration','Ubiquitous Learning and Teaching','Virtual Environments','Vocabulary','Writing']

        cols_length = len(keylist) / 3
        keytable = []
        for i in range(0, len(keylist), cols_length):
            keytable.append(keylist[i:i+cols_length])

        context['keytable'] = keytable
        return context


class SubscriberCreateView(CreateView):
    model = Subscriber
    template_name = 'subscriber_create.html'
    form_class= CreateSubscriberForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Begin reCAPTCHA validation with google.
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
            
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret':  settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = json.load(response)
        # End reCAPTCHA validation 

        if result['success']:
            messages.success(self.request, 'Your email has been registered.', extra_tags='success')
            return super(SubscriberCreateView, self).form_valid(form)
        else:
            messages.error(self.request, 'Invalid reCAPTCHA. Please try again.', extra_tags='danger')
            return super(SubscriberCreateView, self).form_invalid(form)     

        


