from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError


from .models import *
m=Authen()
def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup1.html")
def add(request):
    try:
        name=request.GET['user']
    except MultiValueDictKeyError:
        name = False
    try:
        pas=request.GET['password']
    except MultiValueDictKeyError:
        pas= False
    
    
    m.insert(name,pas)
    return HttpResponse("registered successfully")
    
def user(request):
    try:
        username = request.POST['user']
    except MultiValueDictKeyError:
        username = False
    try:
        password  = request.POST['password']
    except MultiValueDictKeyError:
        password= False
    if m.isvalid(username,password):
        return render(request,'user.html',{"name":username})
    return render(request,'user.html',{"name":"unknown"})
    
    
