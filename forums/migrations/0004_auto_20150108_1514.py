# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_auto_20150107_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(null=True, verbose_name=b'date published', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='lastUpdated',
            field=models.DateTimeField(null=True, verbose_name=b'last updated', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 8, 15, 14, 38, 267284, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
