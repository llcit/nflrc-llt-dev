# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-23 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lltsite', '0007_auto_20180509_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='storypage',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
    ]
