# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-29 18:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0010_remove_movie_release_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='artist_id',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='genre_id',
            new_name='genre',
        ),
    ]