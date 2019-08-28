from rest_framework import serializers
from models import *

class Movie_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_user
        fields = '__all__'