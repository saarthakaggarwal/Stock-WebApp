from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
import finnhub

# Create your views here

def index(request):

    finnhub_client = finnhub.Client(api_key="cb8rlfaad3i0v9a1umlg")
    newsData = finnhub_client.general_news('general', min_id=0)

    first_news = newsData[0]
    second_news = newsData[1]
    third_news = newsData[2]

    first_news_title = first_news["headline"]
    second_news_title = second_news["headline"]
    third_news_title = third_news["headline"]
    
    context = {
        "first_news_title" : first_news_title,
        "second_news_title" : second_news_title,
        "third_news_title" :  third_news_title,
        "first_news_image" : first_news["image"],
        "second_news_image" : second_news["image"],
        "third_news_image" : third_news["image"]
    }

    frontpage_companies = ["AAPL", "AMZN", "TSLA", "MSFT"]

    for symbol in frontpage_companies:
        context[symbol + "_current_price"] = finnhub_client.quote(symbol)["c"]
        context[symbol + "_price_change"] = finnhub_client.quote(symbol)["dp"]


    return render(request, "index.html", context)

def about(request):
    context = {
        "name" : "Saarthak"
    }

    return render(request, "about.html", context)
