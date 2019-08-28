# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.crypto import get_random_string
from models import *
from decorators import *
from django.contrib.auth import logout
from serializers import *
from random import randint

# @api_view(['GET'])
# @renderer_classes((TemplateHTMLRenderer,))
# def admin_login(request):
#     return Response(template_name='login.html')

class admin_login(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    def get(self, request, format=None):
        return Response(template_name='login.html')

    # @checkAdmin
    def post(self, request, format=None):
        return Response(template_name='register.html')

class login(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    def get(self, request, format=None):
        return Response(template_name='login.html')

    @checkAdmin
    def post(self, request, format=None):
        return Response(template_name='register.html')
