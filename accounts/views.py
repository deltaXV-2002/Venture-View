from django.shortcuts import render

# Create your views here.
def register(request):
    render(request,'register.html')