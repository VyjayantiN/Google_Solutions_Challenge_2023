from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import QueryDict
import json
from urllib.parse import unquote
import urllib
from .models import recipe,gen_ins,mother_recipe,mother_ins
# Create your views here.
def home(request):
    return render(request,'accounts/index.html')
def ourword(request):
    return render(request,'accounts/ourword.html')
def about(request):
    return render(request,'accounts/about2.html')
def features(request):
    return render(request,'accounts/features.html')
def mother_bmi(request):
    return render(request,'accounts/mother_bmi.html')
def child_bmi(request):
    return render(request,'accounts/child_bmi.html')
def blog(request):
    return render(request,'accounts/blog.html')
def usermain(request):
    if request.method=='POST':
        height=request.POST['height']
        weight=request.POST['weight']
        age=request.POST['age']
        district=request.POST['district']
        gender=request.POST['gender']
        category=""
        print(request.POST)
        bmi = int(weight) / ((int(height)/100) ** 2)
        print(bmi)
        if gender.lower() == "male":
            if bmi < 18.5:
                category = "Underweight"
            else:
                category = "Healthy"
        elif gender.lower() == "female":
            if bmi < 18.5:
                category = "Underweight"
            else:
                category = "Healthy"
        else:
            category = "Unknown gender"
        object_1=recipe.objects.filter(district=district,age=age)
        object_2=gen_ins.objects.filter(age=age)
        for obj in object_2:
            return render(request,'accounts/usermain.html',{'obj1':object_1,'instructions':obj.instructions,'food_items':obj.food_items,'mal_instructions':obj.mal_ins,'category':category})

def mother(request):
    if request.method=='POST':
        age=request.POST['age']
        height=request.POST['height']
        weight=request.POST['weight']
        district=request.POST['district']
        category=""
        bmi = int(weight) / ((int(height)/100) ** 2)
        if bmi < 18.5:
            category = "Underweight"
        else:
            category = "Healthy"       
        print(district)
        object_1=mother_recipe.objects.filter(district=district,age=age)
        object_2=mother_ins.objects.filter(age=age)
        for obj in object_2:
            return render(request,'accounts/mother.html',{'obj1':object_1,'instructions':obj.instructions,'food_items':obj.food_items,'mal_instructions':obj.mal_ins,'category':category})







def items_home(request):
    my_data = request.GET.get('data', '')
    object_1=recipe.objects.filter(recipe_name=my_data)
    for obj in object_1:
        return render(request,'accounts/item2.html',{'recipe_name':my_data,'ins':obj.ins,'calories':obj.calories,'people_served':obj.people_served,'difficulty':obj.difficulty, 'ing':obj.ing})
def mother_home(request):
    my_data = request.GET.get('data', '')
    object_1=mother_recipe.objects.filter(recipe_name=my_data)
    for obj in object_1:
        return render(request,'accounts/item.html',{'recipe_name':my_data,'ins':obj.ins,'calories':obj.calories,'people_served':obj.people_served,'difficulty':obj.difficulty, 'ing':obj.ing})
    

def post1(request):
    return render(request,'accounts/post1.html')
def post2(request):
    return render(request,'accounts/post2.html')
def post3(request):
    return render(request,'accounts/post3.html')
def post4(request):
    return render(request,'accounts/post4.html')
def post5(request):
    return render(request,'accounts/post5.html')
def post6(request):
    return render(request,'accounts/post6.html')

def yoga1(request):
    return render(request,'accounts/yoga1.html')
def yoga2(request):
    return render(request,'accounts/yoga2.html')
def yoga3(request):
    return render(request,'accounts/yoga3.html')
def yoga4(request):
    return render(request,'accounts/yoga4.html')