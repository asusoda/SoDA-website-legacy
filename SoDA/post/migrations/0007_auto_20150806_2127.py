# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20150806_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='card_image',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='card_image',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='card_image',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
