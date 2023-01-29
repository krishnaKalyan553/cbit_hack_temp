from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path("add",views.add,name='add'),
    path("user",views.user,name='user'),
    path("about",views.about,name='about'),
    path("feedback",views.feedback,name="feedback"),
    path("menu",views.menu,name="menu"),
    path("cart",views.cart,name="cart"),
    path("payment",views.payment,name="payment"),
]