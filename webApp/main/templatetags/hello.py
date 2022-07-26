from django import template

register = template.Library()

@register.filter

def get(dict, arg):
    if arg == "image":
        try:
            return dict["thumbnail"]["resolutions"][0]["url"]
        except:
            return "static/S&P.png"
    if arg == "title":
        return dict["title"]
    if arg == "link":
        return dict["link"]