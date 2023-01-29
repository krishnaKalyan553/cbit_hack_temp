from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path("add",views.add,name='add'),
    path("user",views.user,name='user')
]