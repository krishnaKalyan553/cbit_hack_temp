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
    return render(request,'login.html')
    
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
def cart(request):
    return render(request,'cart.html')
def about(request):
    return render(request,'about.html')
def contacts(request):
    return render(request,'contacts.html')
def menu(request):
    return render(request,'menu.html')
def feedback(request):
    return render(request,'feedback.html')
def payment(request):
    return render(request,'payment.html')
def thankyou(request):
    return render(request,'thankyou.html')
    

def about(request):
    return render(request,"about.html")



def feedback(request):
    return render(request,"feedback.html")


def menu(request):
    return render(request,"menu.html")

def cart(request):
    return render(request,"cart.html")

    
def payment(request):
    return render(request,"payment.html")

    
