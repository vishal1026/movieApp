# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-28 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0006_auto_20190828_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_user',
            name='is_active',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='movie_user',
            name='last_login',
            field=models.DateField(null=True),
        ),
    ]
