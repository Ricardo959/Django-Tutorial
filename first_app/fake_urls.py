## django did not create this file!

from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
