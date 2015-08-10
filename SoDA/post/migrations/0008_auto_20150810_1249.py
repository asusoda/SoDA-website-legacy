# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20150806_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='link_title',
            field=models.CharField(default=b'', max_length=b'100', verbose_name=b'Link name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='announcement',
            name='link_url',
            field=models.URLField(default=b'', verbose_name=b'URL for Link 1', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='link_title',
            field=models.CharField(default=b'', max_length=b'100', verbose_name=b'Link name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='link_url',
            field=models.URLField(default=b'', verbose_name=b'URL for Link 1', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='git_name',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Name of Github repo', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='link_title',
            field=models.CharField(default=b'', max_length=b'100', verbose_name=b'Link name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='link_url',
            field=models.URLField(default=b'', verbose_name=b'URL for Link 1', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='git_link',
            field=models.URLField(verbose_name=b'Link to Github repo', blank=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='vector_image',
            field=models.ImageField(upload_to=b'', verbose_name=b'Image of Company Logo'),
        ),
    ]
