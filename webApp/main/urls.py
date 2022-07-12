from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path("", views.index, name='main'),    
    path("About", views.about, name='main')    

]
