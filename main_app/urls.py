# create this file
# rerouting all requests that have ‘api’ in the url to the <code>apps.core.urls
from django.conf.urls import url
from django.urls import path
from rest_framework import routers

from main_app.views import CustomView
from . import views

router = routers.DefaultRouter()


urlpatterns = [
    url(r'customview', CustomView.as_view()),
   url(r'client/(?P<id>.+)', views.clientslist.as_view()),
    url('login/(?P<login>.+)/(?P<password>.+)', views.login_Client.as_view()),
    path("inscrit",views.client_inscrit.as_view(),name='inscrit'),
    path('update/<int:id>/<str:login>/<str:password>',views.client_upload.as_view(),name='update_client'),
    path('liste_reservation/<int:id>',views.get_reservations.as_view(),name="liste_reservations"),
    path('menu_jour',views.get_menus.as_view(),name="liste_menu_jour"),
    path('articles',views.get_articles.as_view(),name="liste_articles"),
path('add_commande', views.get_post_commandes.as_view(), name='get_post_commandes'),
    path('get_commande/<int:id>',views.get_commandes.as_view()),
path('add_reservation',views.get_post_reservations),
]

urlpatterns += router.urls
