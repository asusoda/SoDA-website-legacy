# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20150810_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='competition_website',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Name of the Competition Website', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='competiton_website_url',
            field=models.URLField(default=b'', verbose_name=b'URL for Competition Website', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='google_map',
            field=models.TextField(default=b'', verbose_name=b'iframe for google map', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='announcement',
            name='card_image',
            field=models.ImageField(upload_to=b'', verbose_name=b'Image for mdl-card__media', blank=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='link_title',
            field=models.CharField(default=b'', max_length=b'100', verbose_name=b'General Link name', blank=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='link_url',
            field=models.URLField(default=b'', verbose_name=b'General URL for Link', blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='card_image',
            field=models.ImageField(upload_to=b'', verbose_name=b'Image for mdl-card__media', blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='link_title',
            field=models.CharField(default=b'', max_length=b'100', verbose_name=b'General Link name', blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='link_url',
            field=models.URLField(default=b'', verbose_name=b'General URL for Link', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='card_image',
            field=models.ImageField(upload_to=b'', verbose_name=b'Image for mdl-card__media', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='link_title',
            field=models.CharField(default=b'', max_length=b'100', verbose_name=b'General Link name', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='link_url',
            field=models.URLField(default=b'', verbose_name=b'General URL for Link', blank=True),
        ),
    ]
