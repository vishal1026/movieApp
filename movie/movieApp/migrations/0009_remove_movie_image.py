# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-29 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0008_auto_20190828_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='image',
        ),
    ]
