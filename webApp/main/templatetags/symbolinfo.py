import finnhub
from django import template
from datetime import date

register = template.Library()


@register.filter
def get_title(symbol):
    finnhub_client = finnhub.Client(api_key="cbiol1iad3i2thcmnhk0")
    data = finnhub_client.company_profile2(symbol=symbol)
    return data["name"]

@register.filter
def get_news(symbol, args):
    finnhub_client = finnhub.Client(api_key="cbiol1iad3i2thcmnhk0")
    dict = finnhub_client.company_news(symbol, _from="2022-01-01", to=date.today())

    arg_list = [arg.strip() for arg in args.split(',')]
    categ = arg_list[0]
    number=int(arg_list[1])

    if categ == "image":
        if dict[number]["image"] == "":
            return "static/NotFound.png"
        return dict[number]["image"]
    if categ == "title":
        return dict[number]["headline"]
    if categ == "link":
        return dict[number]["url"]


