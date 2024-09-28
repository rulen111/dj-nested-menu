from django import template

from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag("menu/nested_menu.html", takes_context=True)
def draw_menu(context, menu_slug):
    target_depth = context["request"].get("item", 0)
    menu_items = MenuItem.objects.select_related("menu").filter(menu__slug=menu_slug, depth__lte=(target_depth + 1)).order_by("depth", "position").all()

    if not menu_items:
        return None



    return
