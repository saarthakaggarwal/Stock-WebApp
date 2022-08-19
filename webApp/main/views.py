from email import message
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
import finnhub
from utils.graphing import makePlot, returnnews
from utils.symbolsearch import symbolexists
from django.urls import resolve
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here



def index(request):

    finnhub_client = finnhub.Client(api_key="cbiol1iad3i2thcmnhk0")
    newsData = finnhub_client.general_news('general', min_id=0)

    plot = makePlot('SPY')
    context = {
    }
    
    try:
        valid_symbol = request.session['valid_symbol']
        context["valid_symbol"] = valid_symbol
        del request.session['valid_symbol']
    except:
        context["valid_symbol"] = True
        pass

    context["plot"] = plot
    SNPData = returnnews()

    j = 1
    for data in SNPData[0:3]:
        context["news" + str(j)] = data
        j += 1

 

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









def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in!")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("/")
     
    return HttpResponse("Error 404: Not Found")

def handleLogout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect("/")







def handleSignup(request):
    if request.method == "POST":
        signupusername = request.POST["signupusername"]
        signuppassword = request.POST["signuppassword"]
        signupemail = request.POST["signupemail"]
        


        myuser = User.objects.create_user(signupusername, signupemail, signuppassword)
        myuser.save()
        messages.success(request, "Your account has been successfully made!")
        return redirect("/")
    else:
        return HttpResponse("Error 404: Not Found")











def about(request):
    context = {
        "name" : "Saarthak"
    }

    return render(request, "about.html", context)


def searchSymbol(request):
    global valid_stock

    current_url = resolve(request.path_info).url_name

    context = {
        
    }

    if request.method == 'POST':
        searched = request.POST["searched"]
        context["symbol"] = searched.upper()

        symbolcheck = symbolexists(searched)
        if symbolcheck:
            finnhub_client = finnhub.Client(api_key="cbiol1iad3i2thcmnhk0")
            context["basic_details"] = finnhub_client.company_profile2(symbol=context["symbol"])
            tempfin = finnhub_client.company_basic_financials(context["symbol"], 'all')["metric"]
            recotemp = finnhub_client.recommendation_trends('AAPL')[0]


            context["plot"] = makePlot(context["symbol"])



            recommendations = {}
            financials = {}
            n=0
            m=0
            for key in recotemp:
                if m > 5:
                    break
                else:
                    recommendations[key] = recotemp[key]
                m += 1


            for key in tempfin:
                new_text = ''
                for i, letter in enumerate(key):
                    if i and letter.isupper():
                        new_text += ' '
                    if i == 0:
                        new_text += letter.upper()
                    else:
                        new_text += letter
                if n > 11:
                    break
                else:
                    n += 1
                    financials[new_text] = tempfin[key]
            context["financials"] = financials
            context["recommendations"] = recommendations

            return render(request, "searchSymbol.html", context)
        else:
            request.session['valid_symbol'] = False
            return redirect(index)
    else:
        return render(request, "index.html", context)

 

