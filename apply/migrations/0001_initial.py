# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('ign', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=20)),
                ('details', models.TextField(max_length=600)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
