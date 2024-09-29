from django import template
from django.utils.html import format_html

from ..models import Menu, MenuItem

register = template.Library()


# @register.inclusion_tag("menu/nested_menu.html", takes_context=True)
# def draw_menu(context, menu_slug):
#     target_depth = context["request"].get("item", 0)
#     menu_items = MenuItem.objects.select_related("menu").filter(menu__slug=menu_slug, depth__lte=(target_depth + 1)).order_by("depth", "position").all()
#
#     if not menu_items:
#         return None
#
#
#
#     return

@register.simple_tag()
def draw_menu(menu_slug):
    menu_items = list(MenuItem.objects.select_related("menu").filter(menu__name=menu_slug))

    if not menu_items:
        return format_html("Menu not found or empty")

    html_string = f"""
    <details>
        <summary><a href='{menu_items[0].menu.url}'>{menu_items[0].menu.name}</a></summary>
           <ul>
                <details>
                    <summary><a href='{menu_items[0].url}'>{menu_items[0].name}</a></summary>
                       <ul>
                            {get_children(menu_items, menu_items[0].pk)}
                       </ul>
                </details>
           </ul>
    </details>
    """

    return format_html(html_string)


def get_children(items, parent_id):
    html_string = ""
    children = [item for item in items if item.parent and item.parent.pk == parent_id]
    for child in children:
        if not child.children:
            html_string += f"<li><a href='{child.url}'>{child.name}</a></li>"
        else:
            html_string += f"""
            <details>
                <summary><a href='{child.url}'>{child.name}</a></summary>
                   <ul>
                        {get_children(items, child.pk)}
                   </ul>
            </details>
            """

    return html_string
