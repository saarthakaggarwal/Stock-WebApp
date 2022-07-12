from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here

def index(request):
    context = {
        "name" : "Saarthak"
    }

    return render(request, "index.html", context)

def about(request):
    context = {
        "name" : "Saarthak"
    }

    return render(request, "about.html", context)
