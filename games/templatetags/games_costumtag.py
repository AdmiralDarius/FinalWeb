from django import template
from math import floor


register = template.Library()


@register.filter()
def formatSeconds(s):
    mins = floor(s / 60);
    secs = floor(s - (mins * 60))
    return "%d:%02d" % (mins, secs)


@register.filter()
def minute(s):
    mins = floor(s / 60);
    return mins

@register.filter()
def multiply(s, arg):
    res = s * arg
    return res

@register.filter()
def divide(s, arg):
    res = s / arg
    return res
