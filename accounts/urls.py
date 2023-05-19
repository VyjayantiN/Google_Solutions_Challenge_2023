from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.home),
    path('about',views.about),
    path('home', views.home),
    path('usermain',views.usermain,name='usermain'),
    path('items_home',views.items_home,name='items_home'),
    path('markdownx/', include('markdownx.urls')),
]