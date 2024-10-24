from django.urls import path
from . import views

urlpatterns = [
    path("register",views.register, name= "register")
    
 ] # whenever you call the home page it will call home(views.home) 