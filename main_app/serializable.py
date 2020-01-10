from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main_app.models import *


class ClientSerializer(serializers.ModelSerializer ):

    class Meta:
        #model = Client

        fields = ('id','nom','prenom','ville','email','date_naissance','login','password')

