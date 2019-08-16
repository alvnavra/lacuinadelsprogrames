from django import template
import re

register = template.Library()

@register.filter(name="change_url")
def change_url(value,idioma):
    rdo = re.sub('^./\w{2}/$',value,'/'+idioma+'/')
    return rdo

@register.filter(name="add_translation_url")
def add_translation_url(value,idioma):
    rdo = ''
    if value.startswith('/ca/'):
        rdo = value.replace('/ca/','/'+idioma+'/')
    elif value.startswith('/es/'):
        rdo = value.replace('/es/','/'+idioma+'/')
    elif value.startswith('/en/'):
        rdo = value.replace('/en/','/'+idioma+'/')
    else:
        rdo = '/'+idioma+value
    return rdo
