# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_short', models.TextField()),
                ('url_long', models.TextField()),
                ('status', models.TextField()),
                ('title', models.TextField()),
            ],
        ),
    ]
