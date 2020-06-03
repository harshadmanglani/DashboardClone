from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dash, name = 'powerbi'),
    path('input/', views.input, name = 'input form'),
    path('inspect/', views.inspect, name = 'inspect') 
]