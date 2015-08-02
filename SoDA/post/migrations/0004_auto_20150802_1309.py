# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20150727_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'Title of post')),
                ('date', models.DateField(verbose_name=b'Date of publication')),
                ('body', models.TextField(verbose_name=b'Text Body of the post')),
                ('location', models.CharField(max_length=100, verbose_name=b'Location of the annuncement', blank=True)),
                ('card_image', models.ImageField(upload_to=b'static/images', blank=True)),
                ('git_link', models.URLField(max_length=100, verbose_name=b'Link to Github repo')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='announcement',
            old_name='image',
            new_name='card_image',
        ),
        migrations.RenameField(
            model_name='competition',
            old_name='image',
            new_name='card_image',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateField(verbose_name=b'Date of publication'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='date',
            field=models.DateField(verbose_name=b'Date of publication'),
        ),
    ]
