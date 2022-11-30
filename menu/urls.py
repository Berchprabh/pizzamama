from django.urls import path
from .import views

#namespacing
app_name = "menu"

urlpatterns = [
    path('', views.index, name="index"),
    # path is default or empty
    # views is the file from which we call the index function
    # which we previously defined
    # we provide a name to this path called index, the
    # benefit of naming will be later made clear
]