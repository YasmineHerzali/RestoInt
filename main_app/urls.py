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
]

urlpatterns += router.urls
