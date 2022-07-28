from django import views
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("home/", views.home, name="home"),
    path('about/', views.about, name='about'),

]
