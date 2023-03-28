from django.db import models

class recipe(models.Model):
    recipe_name=models.CharField(max_length=100,null=True)
    in_1=models.CharField(max_length=15,null=True)
    in_2=models.CharField(max_length=15,null=True)
    in_3=models.CharField(max_length=15,null=True)
    age=models.CharField(max_length=20,null=True)
    category=models.CharField(max_length=50,null=True)
   ' ''image=models.ImageField(upload_to='images/',blank=True)'''
class gen_ins(models.Model):
    instructions=models.TextField()
    food_items=models.TextField()
    mal_ins=models.TextField()
    age=models.CharField(max_length=20,null=True)

