from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,"home/home.html")

def login(request):
    # username = request.POST["username"]
    # password  = request.POST["password"]
    pass



def signin(request):
    # username = request.POST["username"]
    # password  = request.POST["password"]
    
    pass

def signout(request):
    pass

