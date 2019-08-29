# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.crypto import get_random_string
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from models import *
from decorators import *
from serializers import *
from random import randint
from datetime import datetime

@api_view(['GET','POST'])
@checkAdmin
@renderer_classes((TemplateHTMLRenderer,))
def admin_profile(request):
    if request.method == 'GET':
        template = { 1:'superAdmin/super_admin.html', 2:'admin/admin.html' }
        return render(request,template[request.session['user_type']])
    elif request.method == 'POST':
        print request




@api_view(['GET'])
@checkAdmin
@renderer_classes((TemplateHTMLRenderer,))
def add_admin(request):
    if request.method == 'GET':
        template = { 1:'superAdmin/super_admin.html', 2:'admin/admin.html' }
        return render(request,template[request.session['user_type']])
    elif request.method == 'POST':
        print request

class login(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    def get(self, request):
        return Response(template_name='login.html')

    def post(self, request):
        try:
            user = Movie_user.objects.get(user_name = request.data['user_name'], password=request.data['password'])
            request.session['first_name'] = user.first_name
            request.session['first_name'] = user.first_name
            request.session['user_type'] = user.user_type
            request.session['user_name'] = user.user_name
            user.last_login = datetime.now()
            user.save()
            template = 'super_admin.html' if user.user_type==1 else 'admin.html'
        except  Movie_user.DoesNotExist:
            return Response({'invalidCredential':True},template_name='login.html')
        # return Response(template_name=template)
        return HttpResponseRedirect('/movieApp/admin_profile/')
