# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='location_boolean',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='location_boolean',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='image',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
