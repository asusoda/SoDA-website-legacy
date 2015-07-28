# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'Title of post')),
                ('date', models.DateField(auto_now_add=True, verbose_name=b'Date of publication')),
                ('body', models.TextField(verbose_name=b'Text Body of the post')),
                ('location', models.CharField(max_length=100, verbose_name=b'Location of the annuncement')),
                ('location_boolean', models.BooleanField(default=False, verbose_name=b'Will this post have a location')),
                ('image', models.ImageField(default=False, upload_to=b'')),
                ('headline', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'Title of post')),
                ('date', models.DateField(auto_now_add=True, verbose_name=b'Date of publication')),
                ('body', models.TextField(verbose_name=b'Text Body of the post')),
                ('location', models.CharField(max_length=100, verbose_name=b'Location of the annuncement')),
                ('location_boolean', models.BooleanField(default=False, verbose_name=b'Will this post have a location')),
                ('image', models.ImageField(default=False, upload_to=b'')),
                ('competition_type', models.CharField(default=b'General Hacks', max_length=50, choices=[(b'Past Travel Hacks', b'Past Travel Hackathon'), (b'Current Travel Hack', b'Current SoDA Travel Hackathon'), (b'Past Offical SoDA Hack', b'Past Offical SoDA Coding Competiton'), (b'Current Offical SoDA Hack', b'Current Offical SoDA Hackathon'), (b'General Hacks', b'General Hackathons and Coding Competitons')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
