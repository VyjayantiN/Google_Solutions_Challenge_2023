from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import recipe,gen_ins
# Create your views here.
def home(request):
    return render(request,'accounts/home2.html')
def about(request):
    return render(request,'accounts/about2.html')
def usermain(request):
    if request.method=='POST':
        height=request.POST['height']
        weight=request.POST['weight']
        age=request.POST['age']
        district=request.POST['district']
        gender=request.POST['gender']
        category=""
        bmi = weight / (height ** 2)
        if gender.lower() == "male":
            if bmi < 18.5:
                category = "underweight"
            else:
                category = "healthy"
        elif gender.lower() == "female":
            if bmi < 18.5:
                category = "Underweight"
            else:
                category = "Normal weight"
        else:
            category = "Unknown gender"
        object_1=recipe.objects.filter(age=age,category=category)
        object_2=gen_ins.objects.filter(age=age)
        return render(request,'usermain.html',{'object_1':object_1,'object_2':object_2})
def items_home(request):
    return render(request,'accounts/items_home.html')
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
