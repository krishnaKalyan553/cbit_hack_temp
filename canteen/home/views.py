from django.shortcuts import render
from django.http import HttpResponse

from .models import *
m=Authen()
def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup1.html")
def add(request):
    name=request.GET['user']
    pas=request.GET['password']
    m.insert(name,pas)
    return HttpResponse("registered successfully")
    
def user(request):
    username = request.POST["user"]
    password  = request.POST["password"]
    if m.isvalid(username,password):
        return render(request,'user.html',{"name":username})
    return render(request,'user.html',{"name":"unknown"})
    
    
