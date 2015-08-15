# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20150814_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='competiton_website_url',
            new_name='competition_website_url',
        ),
    ]
