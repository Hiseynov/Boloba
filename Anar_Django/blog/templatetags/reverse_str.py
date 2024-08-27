from django import template

register = template.Library()

@register.simple_tag()
def anyFunction(value):
    return value[::-1]