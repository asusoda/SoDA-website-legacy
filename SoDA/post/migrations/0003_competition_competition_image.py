# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_competition_competition_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='competition_image',
            field=models.ImageField(default='', upload_to=b'', verbose_name=b'Optional Card image for the competition', blank=True),
            preserve_default=False,
        ),
    ]
