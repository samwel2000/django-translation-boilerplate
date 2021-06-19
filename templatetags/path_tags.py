# create path tags for url mapping
from django import template

register = template.Library()

@register.simple_tag
def get_path(path, string):
    split_path = path.split('/')
    current_code = split_path[1]
    full_path = path.replace(f'/{current_code}/',f'/{string}/')
    return full_path