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
                ('announcement_title', models.CharField(max_length=100, verbose_name=b'Title of the Announcement')),
                ('announcement_date', models.DateField(verbose_name=b'Date of Publication')),
                ('announcement_body', models.TextField(verbose_name=b'Body of the Announcement')),
                ('announcement_image', models.ImageField(upload_to=b'', verbose_name=b'Optional Image for the Announcement', blank=True)),
                ('announcement_location', models.TextField(verbose_name=b'Optional iFrame map (Set width to auto and height to 486)', blank=True)),
                ('link1', models.URLField(verbose_name=b'Optional Link', blank=True)),
                ('link1_name', models.CharField(max_length=100, verbose_name=b'Optional Link Name', blank=True)),
                ('link2', models.URLField(verbose_name=b'Optional Link', blank=True)),
                ('link2_name', models.CharField(max_length=100, verbose_name=b'Optional Link Name', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('competition_name', models.CharField(unique=True, max_length=50, verbose_name=b'Name of the Competition')),
                ('competiton_basic_information', models.TextField(verbose_name=b'General Information about the competition')),
                ('competition_website', models.URLField(verbose_name=b'URL for competition website')),
                ('competition_website_name', models.CharField(max_length=100, verbose_name=b'Name of the Website')),
                ('competition_map', models.TextField(verbose_name=b'iFrame for location(Set the width to auto and height to 486)')),
                ('competition_location_info', models.TextField(verbose_name=b'Location and time for the event')),
                ('travel_information', models.TextField(verbose_name=b'Information about Traveling to the Event', blank=True)),
                ('travel_map', models.TextField(verbose_name=b'iFrame map for where we will be meeting to travel to the event', blank=True)),
                ('competition_type', models.CharField(default=b'upcoming hacks', max_length=50, choices=[(b'past hacks', b'Past Hackathons/Coding Competitions'), (b'upcoming hack', b'Future Hackathons/Coding Competitions')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_title', models.CharField(max_length=100, verbose_name=b'Project Title')),
                ('project_image', models.ImageField(upload_to=b'', verbose_name=b'Optional Image for the project', blank=True)),
                ('project_body', models.TextField(verbose_name=b'Descriptiong of the project')),
                ('git_name', models.CharField(default=b'', max_length=100, verbose_name=b'Name of Github repo', blank=True)),
                ('git_link', models.URLField(verbose_name=b'Link to Github repo', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sponsor_name', models.CharField(max_length=100, verbose_name=b'Name of Sponsor')),
                ('sponsorship_tier', models.CharField(default=b'Gold', max_length=100, verbose_name=b'Sponsorship Tier', choices=[(b'Gold', b'Gold'), (b'Silver', b'Silver'), (b'Bronze', b'Bronze')])),
                ('vector_image', models.ImageField(upload_to=b'', verbose_name=b'Image of Company Logo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
