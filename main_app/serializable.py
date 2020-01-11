from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main_app.models import *


class ClientSerializer(serializers.ModelSerializer ):

    class Meta:
        model = Client
        fields = ('id','nom','prenom','adresse','email','login','password')

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reservation
        fields = '__all__'

