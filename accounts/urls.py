from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.home),
    path('about',views.about),
    path('home', views.home),
    path('features', views.features),
    path('usermain',views.usermain,name='usermain'),
    path('items_home',views.items_home,name='items_home'),
    path('mother_home',views.mother_home,name='mother_home'),
    path('mother',views.mother,name='mother'),
    path('mother_bmi', views.mother_bmi),
    path('child_bmi', views.child_bmi),
]