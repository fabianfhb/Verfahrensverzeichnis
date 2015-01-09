# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Verfahrensverzeichnis', '0002_auto_20150108_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='version',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='datum',
            field=models.DateField(default=datetime.datetime(2015, 1, 8, 9, 50, 0, 96006)),
            preserve_default=True,
        ),
    ]
