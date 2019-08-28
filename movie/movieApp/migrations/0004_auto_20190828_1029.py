# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-28 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0003_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='artist_id',
            field=models.ManyToManyField(to='movieApp.Artist'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre_id',
            field=models.ManyToManyField(to='movieApp.Genre'),
        ),
    ]