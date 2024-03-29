# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-28 10:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0002_auto_20190828_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('created_on', models.DateField(default=datetime.datetime.now)),
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('release_date', models.DateField()),
                ('artist_id', models.ManyToManyField(related_name='movies_artist', to='movieApp.Artist')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieApp.Movie_user')),
                ('genre_id', models.ManyToManyField(related_name='movies_genres', to='movieApp.Genre')),
            ],
            options={
                'db_table': 'movie',
            },
        ),
    ]
