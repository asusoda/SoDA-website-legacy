# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20150820_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_post_date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Date Project was started'),
            preserve_default=True,
        ),
    ]
