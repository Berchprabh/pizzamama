from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza

# Create your views here.

# /menu : we have to explain to django that for the url of
# /menu it has to use the index function defined below,
# which sends a request to get an HttpResponse as a string
def index(request):
    '''
    pizzas = Pizza.objects.all() # gets all objects of Pizza
    pizza_names_and_price = [pizza.name + " : " + str(pizza.price)  + "$" for pizza in pizzas] # get only the names of pizzas
    pizza_names_and_price_str = ", ".join(pizza_names_and_price) # join the pizza names separated by comma
    return HttpResponse("Our pizzas - - - - - - : "+ pizza_names_and_price_str) # return pizza names from db
    '''
    pizzas = Pizza.objects.all().order_by('price') 
    # gets all objects of Pizza ordered by the values in the field price
    return render(request,'menu/index.html',{'pizzas':pizzas})

def api_get_pizzas(request):
    pizzas = Pizza.objects.all().order_by('price') # gets all pizza objects
    json = serializers.serialize("json", pizzas) # converts objects to json format
    return HttpResponse(json) # returns json object as a HttpResponse