
from django import template

register = template.Library()

@register.filter(name='remove_special')
def remove_city(value, arg):
    for character in arg:
        value = value.replace(character, "")
    return value

