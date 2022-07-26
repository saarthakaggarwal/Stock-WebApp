from django import template

register = template.Library()

@register.filter
def hello(dict, arg):
    if arg == "image":
        print(dict["thumbnail"]["resolutions"][0]["url"])
        return dict["thumbnail"]["resolutions"][0]["url"]