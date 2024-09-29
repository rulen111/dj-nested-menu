from django import template
from django.utils.html import format_html

from ..models import MenuItem

register = template.Library()


@register.simple_tag()
def draw_menu(menu_name):
    """
    Simple tag function for rendering specified menu from DB.
    :param menu_name: "name" attribute for Menu table
    :return: html string to be rendered
    """
    # Get all items of the specified menu
    menu_items = list(MenuItem.objects.select_related("menu").filter(menu__name=menu_name).order_by("parent", "-sort"))

    # Return error message if no items were found
    if not menu_items:
        return format_html("Menu not found or empty")

    # Construct menu from top level to last child
    top_level = ""
    for item in menu_items:
        if not item.parent:
            if not get_children_list(menu_items, item.pk):
                top_level += f"<li><a href='{item.url}'>{item.name}</a></li>"
            else:
                top_level += f"""
                <details>
                    <summary><a href='{item.url}'>{item.name}</a></summary>
                        <ul>
                            {get_children(menu_items, item.pk)}
                        </ul>
                </details>
                """
        else:
            break

    # Define the root and add the rest of the menu
    html_string = f"""
    <details>
        <summary><a href='{menu_items[0].menu.url}'>{menu_items[0].menu.name}</a></summary>
           <ul>
                {top_level}
           </ul>
    </details>
    """

    return format_html(html_string)


def get_children(items, parent_id):
    """
    Utility function to add all child nodes to html string recursively
    :param items: DB objects of MenuItem table
    :param parent_id: primary key of the parent node
    :return: html string to be added to render
    """
    html_string = ""

    # Find and process child nodes
    children = get_children_list(items, parent_id)
    for child in children:
        if not get_children_list(items, child.pk):
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


def get_children_list(items, parent_id):
    return [item for item in items if item.parent and item.parent.pk == parent_id]
