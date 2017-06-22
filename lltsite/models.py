from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel


class StoryPage(TimeStampedModel):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    thumbnail_desc = models.CharField(
        max_length=160, default='more...', null=True, blank=True, )
    image = models.CharField(max_length=100L, blank=True, default='icon.png',
                             verbose_name='Icon image file name')
    listing_rank = models.IntegerField(blank=True, default=0, help_text='default rank. higher the number, lower the rank')
    featured = models.BooleanField(blank=True, default=False)
    featured_rank = models.IntegerField(blank=True, default=0, help_text='higher the number, lower the rank')
    headline = models.BooleanField(default=False)
    headline_tag = models.CharField(
        max_length=512, blank=True, null=True, default='')
    # tags = generic.GenericRelation(TaggedItem)
    private = models.BooleanField(default=False, blank=True, help_text='checking this ON will require a user to login to view this story')

    def get_absolute_url(self):
        return reverse('page_view', args=[str(self.id)])

    def __unicode__(self):
        return self.title