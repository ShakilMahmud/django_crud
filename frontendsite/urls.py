# from xml.etree.ElementInclude import include

from django.urls import path
from . import views

urlpatterns = [

    path('', views.list, name='list'),
]
