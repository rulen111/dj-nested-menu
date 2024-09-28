from django import template

from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag("menu/nested_menu.html", takes_context=True)
def draw_menu(context, menu_slug):


    return
