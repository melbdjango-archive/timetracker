# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20140916_0736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Entries'},
        ),
        migrations.AddField(
            model_name='entry',
            name='project',
            field=models.ForeignKey(blank=True, to='tracker.Project', null=True),
            preserve_default=True,
        ),
    ]
