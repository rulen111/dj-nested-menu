from django.db import models
from django.conf import settings


class Menu(models.Model):
    """
    Model for Menu table, containing menu name and url
    Used for one-to-many relationship with MenuItem table
    """
    name = models.CharField(max_length=50, unique=True, verbose_name="Menu name")
    url = models.URLField(default=settings.DEFAULT_MENU_URL, verbose_name="Menu url")

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Model for MenuItem table, containing item-to-item and item-to-menu relationship, name and url
    Attribute "sort" can be used for sorting elements on the same depth level
    """
    parent = models.ForeignKey(
        "self", blank=True, null=True, related_name="children", on_delete=models.CASCADE, verbose_name="Parent node"
    )
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE, verbose_name="Menu tree")

    name = models.CharField(max_length=50, verbose_name="Item name")
    sort = models.IntegerField(default=0, verbose_name="Item sorting parameter")
    url = models.URLField(default=settings.DEFAULT_MENU_URL, verbose_name="Item url")

    class Meta:
        verbose_name = "Menu item"
        verbose_name_plural = "Menu items"

    def __str__(self):
        return self.name
