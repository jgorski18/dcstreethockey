# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-03 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0015_auto_20170302_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='gamenumber',
            new_name='weeknumber',
        ),
        migrations.RenameField(
            model_name='matchup',
            old_name='game',
            new_name='week',
        ),
        migrations.RenameModel(
            old_name='game',
            new_name='week',
        ),
    ]