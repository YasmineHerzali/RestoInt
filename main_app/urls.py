# create this file
# rerouting all requests that have ‘api’ in the url to the <code>apps.core.urls
from django.conf.urls import url
from rest_framework import routers

from main_app.views import CustomView
from . import views

router = routers.DefaultRouter()


urlpatterns = [
    url(r'customview', CustomView.as_view()),
    url(r'client/(?P<id>.+)', views.clientslist.as_view())
]

urlpatterns += router.urls
