from django.db import models

class recipe(models.Model):
    recipe_name=models.CharField(max_length=100,null=True)
    people_served=models.TextField(null=True)
    calories= models.TextField(null=True)
    difficulty = models.TextField(null=True)
    ing=models.TextField(null=True)
    ins=models.TextField(null=True)
    age=models.CharField(max_length=20,null=True)
    category=models.CharField(max_length=50,null=True)
    district=models.CharField(max_length=50,null=True)
class gen_ins(models.Model):
    instructions=models.TextField()
    food_items=models.TextField()
    mal_ins=models.TextField()
    age=models.CharField(max_length=20,null=True)
class mother_recipe(models.Model):
    recipe_name=models.CharField(max_length=100,null=True)
    people_served=models.TextField(null=True)
    calories= models.TextField(null=True)
    difficulty = models.TextField(null=True)
    ing=models.TextField(null=True)
    ins=models.TextField(null=True)
    age=models.CharField(max_length=20,null=True)
    category=models.CharField(max_length=50,null=True)
    district=models.CharField(max_length=50,null=True)
class mother_ins(models.Model):
    instructions=models.TextField()
    food_items=models.TextField()
    mal_ins=models.TextField()
    age=models.CharField(max_length=20,null=True)