from django.contrib import admin
from .models import recipe,gen_ins,mother_recipe,mother_ins
# Register your models here.
"""
from .models import Person
admin.site.register(Person)
"""
admin.site.register(recipe)
admin.site.register(gen_ins)
admin.site.register(mother_recipe)
admin.site.register(mother_ins)

