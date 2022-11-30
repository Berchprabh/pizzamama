from django.contrib import admin
from .models import Pizza
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    # create a tuple with value names from models.py
    list_display = ('name','ingredients','vegetarian','price')
    # this generates a searchfield to search by the name of the
    # pizza in the admin backend.
    search_fields = ['name']


admin.site.register(Pizza, PizzaAdmin) 
# adds model of Pizza to the admin site