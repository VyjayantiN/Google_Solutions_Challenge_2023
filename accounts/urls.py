from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('about',views.about),
    path('home', views.home),
    path('user_data',views.user_data,name="user_data")
]