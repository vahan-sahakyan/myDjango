# from django.urls import path, include
import sys
from django.conf.urls import url
from .views import index


urlpatterns = [
    url(r'^$', index, name='index'),
]
