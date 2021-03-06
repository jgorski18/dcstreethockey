# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-18 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0017_auto_20170304_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stat',
            name='en',
        ),
        migrations.AddField(
            model_name='stat',
            name='empty_net',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='goals',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='assists',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='goals_against',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='matchup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leagues.MatchUp'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leagues.Team'),
        ),
    ]
