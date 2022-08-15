from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path("", views.index, name='main'),    
    path("about", views.about, name='About'),  
    path("searchsymbol", views.searchSymbol, name='search'),
    path("signup", views.handleSignup, name = 'handleSignup')
]
