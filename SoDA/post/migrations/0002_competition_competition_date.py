# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='competition_date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Date for the Competition'),
            preserve_default=True,
        ),
    ]
