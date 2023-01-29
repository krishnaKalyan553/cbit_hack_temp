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
    name=request.GET['usr']
    pas=request.GET['pswd']
    m.insert(name,pas)
    return render(request,'login.html')
    
def user(request):
    username = request.POST['name']
    password  = request.POST['pas']
    if m.isvalid(username,password):
        return render(request,'user.html',{"name":username})
    else:
        return render(request,'signup1.html')
def review(request):
    fname=request.GET['firstname']
    rev=request.GET['subject']
    m.addreview(fname,rev)
    return render(request,'home.html')
def cart(request):
    return render(request,'cart.html')
def about(request):
    return render(request,'about.html')
def contacts(request):
    return render(request,'contacts.html')
def menu(request):
    return render(request,'menu.html')
def feedback(request):
    reviews=m.fetchreview()
    print(reviews)
    return render(request,'feedback.html',{'reviews':reviews})
def payment(request):
    return render(request,'payment.html')
def thankyou(request):
    return render(request,'thankyou.html')
def about(request):
    return render(request,"about.html")
def menu(request):
    return render(request,"menu.html")
def cart(request):
    return render(request,"cart.html")   
def payment(request):
    return render(request,"payment.html")

    
