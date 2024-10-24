from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name= "index")
    
 ] # whenever you call the home page it will call home(views.home) 