# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='end_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 16, 7, 36, 41, 837037)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
