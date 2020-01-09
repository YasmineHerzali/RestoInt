from django.http import response
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from rest_framework.views import APIView, Response

from main_app import serializable
from main_app.models import Client


def hello(request,id):
    client=Client.objects.all()
    return render(request,'index.html',{'client':client})


class clientslist(APIView):
    def get(self,request,id,format=None):
        clients=Client.objects.get(id=id)

        return Response(clients.__str__())
    def post(self,request,format=None):
        pass

class login_Client(APIView):
    def get(self,request,login,password,format=None):
        clients=Client.objects.filter(login=login)

        return Response(clients.__str__())
    def post(self,request,format=None):
        pass


class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Some Get Response")

    def post(self, request, format=None):
        return Response("Some Post Response")