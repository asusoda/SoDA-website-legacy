# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20150802_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sponsor_name', models.CharField(max_length=100, verbose_name=b'Name of Sponsor')),
                ('sponsorship_tier', models.CharField(default=b'Gold', max_length=100, verbose_name=b'Sponsorship Tier', choices=[(b'Gold', b'Gold'), (b'Silver', b'Silver'), (b'Bronze', b'Bronze')])),
                ('vector_image', models.ImageField(upload_to=b'static/images', verbose_name=b'Image of Company Logo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
