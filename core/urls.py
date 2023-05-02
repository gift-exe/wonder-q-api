from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("posts",views.details_page,name='details'),
    path("",views.index,name='home2'),
]