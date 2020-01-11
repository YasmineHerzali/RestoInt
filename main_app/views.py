from django.shortcuts import render
from pip._vendor.pytoml.parser import _p_key
from rest_framework.generics import ListCreateAPIView
from django.http import JsonResponse

from django.core import serializers

# Create your views here.
from rest_framework import viewsets, status

from rest_framework.response import Response
from django.http.response import HttpResponse

from rest_framework.views import APIView


from main_app.models import Client, Reservation, Menu, Element, Commande
from main_app.serializable import ClientSerializer, CommandeSerializer, ReservationSerializer


def hello(request,id):
    client=Client.objects.all()
    return render(request,'index.html',{'client':client})


class clientslist(APIView):
    def get(self,request,id,format=None):
        clients=Client.objects.get(id=id)

        return Response(clients.__str__())


class login_Client(APIView):
    def get(self,request,login,password):

        client=Client.objects.filter(login=login).filter(password=password)
        if client is None:
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            res=serializers.serialize('json', client)
            return HttpResponse(res)






class client_inscrit(ListCreateAPIView):
    serializer_class = ClientSerializer
    def get_queryset(self):
        serializer_class=ClientSerializer(self.request)
        if(serializer_class.is_valid()):
            client=serializer_class.save()
            res=serializers.serialize('json',client)
            return HttpResponse(res)
        else:
            return Response({'status':'erreur'},status=status.HTTP_400_BAD_REQUEST)


class client_upload(APIView):
    def get(self,request,id,login,password):
            client=Client.objects.get(id=id)
            print(client)
            if client is None:
                return Response({'status': 'erreur'}, status=status.HTTP_400_BAD_REQUEST)

            else:
                client.__setattr__('login', login)
                client.__setattr__('password', password)
                client.save()
                res=serializers.serialize('json',client)
                return HttpResponse(res)



def to_json(listes):
    if len(listes)==0:
        return "[]"
    else:
        res="["
        for item in listes:
            res+=item.__str__()+","
        res=res[0:(len(res)-1):1]
        res+="]"
        return res


class get_reservations(APIView):
    def get(self,request,id):
        client=Client.objects.get(id=id)
        reservations=Reservation.objects.filter(client=client)
        if reservations is not None:
            res=serializers.serialize('json',reservations)
            return HttpResponse(to_json(reservations))
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)



class get_menus(APIView):
    def get(self,request):
        menus=Menu.objects.filter(type="menu du jour")
        if menus is not None:

            return Response(to_json(menus))
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

class get_articles(APIView):
    def get(self,request):
        articles=Element.objects.filter(menu__type__exact='plat')
        if articles is not None:
            res=serializers.serialize('json',articles)
            return HttpResponse(to_json(articles))
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)



class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Some Get Response")

    def post(self, request, format=None):
        return Response("Some Post Response")


class get_post_commandes(ListCreateAPIView):
    serializer_class = CommandeSerializer

    def get_queryset(self):
        serializer_class=CommandeSerializer(self.request)
        commande=serializer_class.save()
        return HttpResponse(serializers.serialize('json',commande))

class get_commandes(APIView):
    def get(self,request,id):
        client=Client.objects.get(id=id)
        commandes=Commande.objects.filter(client=client)
        if commandes is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            res=serializers.serialize('json',commandes)
            return HttpResponse(to_json(commandes))

class get_post_reservations(ListCreateAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        serializer_class=ReservationSerializer(self.request)
        reservation=serializer_class.save()
        return HttpResponse(serializers.serialize('json',reservation))

