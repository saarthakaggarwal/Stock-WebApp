from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
import finnhub
from utils.graphing import test, test2

# Create your views here

def index(request):

    finnhub_client = finnhub.Client(api_key="cb8rlfaad3i0v9a1umlg")
    newsData = finnhub_client.general_news('general', min_id=0)

    plot = test()
    context = {
    }
    context["plot"] = plot

    news = ["first_news", "second_news", "third_news"]
    n = 0
    for head in news:
        context[head + "_title"] = newsData[n]["headline"]
        context[head + "_image"] = newsData[n]["image"]
        context[head + "_url"] = newsData[n]["url"]
        n += 1

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
