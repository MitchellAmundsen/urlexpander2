# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-15 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlexpanderapp', '0002_auto_20160815_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='recent',
            field=models.DateTimeField(default='N/A'),
        ),
    ]