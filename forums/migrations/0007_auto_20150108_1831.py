# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0006_auto_20150108_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(null=True, blank=True, verbose_name='date published'),
            preserve_default=True,
        ),
    ]
