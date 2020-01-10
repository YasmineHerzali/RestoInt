from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView




# Create your views here.
from rest_framework import viewsets, status

from rest_framework.response import Response

from rest_framework.views import APIView


from main_app.models import Client
from main_app.serializable import ClientSerializer



def hello(request,id):
    client=Client.objects.all()
    return render(request,'index.html',{'client':client})


class clientslist(APIView):
    def get(self,request,id,format=None):
        clients=Client.objects.get(id=id)

        return Response(clients.__str__())


class login_Client(APIView):
    def get(self,request,login,password,format=None):

        client=Client.objects.filter(login=login).filter(password=password)
        if client is None:
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(client.__str__())






class client_inscrit(ListCreateAPIView):
    serializer_class = ClientSerializer
    def get_queryset(self):
        serializer_class=ClientSerializer(self.request)
        if(serializer_class.is_valid()):
            client=serializer_class.save()
            return Response(client)
        else:
            return Response({'status':'erreur'},status=status.HTTP_400_BAD_REQUEST)


class client_upload(APIView):
    def get(self,request,id,login,password):
            client=Client.objects.get(id=id)
            if client is not None:
                client.__setattr__('login',login)
                client.__setattr__('password',password)
                client.save()
                return Response(client.__str__())
            else:
                return Response({'status':'erreur'},status=status.HTTP_400_BAD_REQUEST)


class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Some Get Response")

    def post(self, request, format=None):
        return Response("Some Post Response")