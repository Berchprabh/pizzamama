from django.urls import path
from .import views

urlpatterns = [
    path('GetPizzas',views.api_get_pizzas)
]