# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class Movie_user(models.Model):
	user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=70)
	last_name = models.CharField(max_length=70)
	user_name = models.CharField(max_length=70, unique = True)
	password = models.CharField(max_length=70)
	is_active = models.IntegerField(default=0)
	user_type = models.IntegerField()
	created_on = models.DateField(default=datetime.now)
	last_login = models.DateField(null=True)

	class Meta:
		db_table = 'movie_user'

class Common_create(models.Model):
    created_on = models.DateField(default=datetime.now)
    created_by = models.ForeignKey( Movie_user)

    class Meta:
        abstract = True

class Genre(Common_create):
	genre_id  = models.AutoField(primary_key=True)
	genre_type = models.CharField(max_length=50, unique = True)

	class Meta:
		db_table = 'genre'

class Artist(Common_create):
	artist_id  = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	class Meta:
		db_table = 'artist'


class Movie(Common_create):
	movie_id  = models.AutoField(primary_key=True)
	movie_name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	genre  = models.ManyToManyField(Genre)
	artist = models.ManyToManyField(Artist)

	class Meta:
		db_table = 'movie'
