# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_competition_competition_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='competiton_basic_information',
            new_name='competition_basic_information',
        ),
    ]
