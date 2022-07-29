import finnhub
from django import template

register = template.Library()

@register.filter
def get_title(symbol):
    finnhub_client = finnhub.Client(api_key="cb8rlfaad3i0v9a1umlg")
    symboldata = finnhub_client.symbol_lookup(symbol)
    title = symboldata['result'][0]['description']
    return title 
