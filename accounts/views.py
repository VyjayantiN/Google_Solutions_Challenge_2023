from django.shortcuts import render,redirect
from django.http import HttpResponse

#from .models import Person
# Create your views here.
def home(request):
    return render(request,'accounts/home.html')
def about(request):
    return render(request,'accounts/about.html')
"""
def user_data(request):
    if(request.method=='POST'):
        height=request.POST['height']
        weight=request.POST['weight']
        gender = request.POST['gender']
        district = request.POST['district']
        age = request.POST['age']
        my_model =Person.objects.create(height=height, weight=weight,gender=gender,district=district,age=age)
        my_model.save()
  """                      
