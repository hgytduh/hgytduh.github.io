# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0004_auto_20150108_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(verbose_name='date published', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='lastUpdated',
            field=models.DateTimeField(verbose_name='last updated', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(to='forums.Topic', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(verbose_name='date published'),
            preserve_default=True,
        ),
    ]
