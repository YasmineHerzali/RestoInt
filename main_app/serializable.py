from rest_framework import serializers

from main_app.models import Client


class clientserializer(serializers.ModelSerializer ):
    class Meta:
        model= Client
        fields= '__all__'