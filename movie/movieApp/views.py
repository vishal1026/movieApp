# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render
from models import *
from decorators import *
from serializers import *
from datetime import datetime

class login(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    def get(self, request):
        return Response(template_name='login.html', status=status.HTTP_200_OK)

    def post(self, request):
        try:
            user = Movie_user.objects.get(user_name = request.data['user_name'], password=request.data['password'])
            request.session['first_name'] = user.first_name
            request.session['first_name'] = user.first_name
            request.session['user_type'] = user.user_type
            request.session['user_name'] = user.user_name
            request.session['user_id'] = user.user_id
            user.last_login = datetime.now()
            user.save()
        except  Movie_user.DoesNotExist:
            return Response({'invalidCredential':True},template_name='login.html' , status=status.HTTP_404_NOT_FOUND)
        # return Response(template_name=template)
        return HttpResponseRedirect('/movieApp/admin_profile/')

class home(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    def get(self, request):
        return Response(template_name='home.html', status=status.HTTP_200_OK,
        data={
            'movies' : MovieSerializer(Movie.objects.all(), many=True).data
        })

    def post(self, request):
        if 'getMovie' in request.POST:
            return Response(template_name='home.html', status=status.HTTP_200_OK,
            data={
                'movies' : MovieSerializer(Movie.objects.filter(movie_name__contains=request.POST['searchMovie']), many=True).data
            })

@api_view(['GET','POST'])
@checkAdmin
@renderer_classes((TemplateHTMLRenderer,))
def admin_profile(request):
    if request.method == 'GET':
		return render(request, 'admin/admin.html',
        {
			'artists' : ArtistSerializer(Artist.objects.all(), many=True).data,
			'genres' : GenreSerializer(Genre.objects.all(), many=True).data
        })

    elif request.method == 'POST':
        msg = {}
        if 'addGenre' in request.POST:
            genre = GenreSerializer(data = request.POST)
            if genre.is_valid():
                genre.save()
            else:
                msg = genre.error

        if 'addArtist' in request.POST:
            artist = ArtistSerializer(data = request.POST)
            if artist.is_valid():
                artist.save()
            else:
                msg = artist.error

        if 'addMovie' in request.POST:
            artist_list = request.POST.getlist('artist_id',[])
            genre_list = request.POST.getlist('artist_id',[])
            movie = Movie()
            movie.movie_name = request.POST['movie_name']
            movie.description = request.POST['description']
            movie.created_by_id = request.POST['created_by']
            movie.save()

            for genre_id in genre_list:
                genre_obj = Genre.objects.get(genre_id=genre_id)
                movie.genre.add(genre_obj)

            for artist_id in artist_list:
                artist_obj = Artist.objects.get(artist_id=artist_id)
                movie.artist.add(artist_obj)

    return HttpResponseRedirect('/movieApp/admin_profile/')


@api_view(['POST'])
@checkSuperAdmin
@renderer_classes((TemplateHTMLRenderer,))
def add_admin(request):
    form_data = request.POST
    user = Movie_userSerializer(data = request.POST )
    if user.is_valid():
        user.save()
    else:
        return render(request, 'admin/admin.html',user.error)
    return render(request, 'admin/admin.html' )

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/movieApp/')