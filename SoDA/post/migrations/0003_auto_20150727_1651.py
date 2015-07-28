# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20150721_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(upload_to=b'static/images', blank=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='location',
            field=models.CharField(max_length=100, verbose_name=b'Location of the annuncement', blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='competition_type',
            field=models.CharField(default=b'upcoming hacks', max_length=50, choices=[(b'past hacks', b'Past Hackathons/Coding Competitions'), (b'upcoming hack', b'Future Hackathons/Coding Competitions')]),
        ),
        migrations.AlterField(
            model_name='competition',
            name='image',
            field=models.ImageField(upload_to=b'static/images', blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='location',
            field=models.CharField(max_length=100, verbose_name=b'Location of the annuncement', blank=True),
        ),
    ]
