# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-15 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlexpanderapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='recent',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='url',
            name='snapshot',
            field=models.TextField(default='N/A'),
        ),
    ]