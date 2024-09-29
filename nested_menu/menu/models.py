from django.db import models
from django.conf import settings


class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name="Menu name")
    # slug = models.SlugField(max_length=50, blank=True, null=True, verbose_name="Menu slug name")
    url = models.URLField(default=settings.DEFAULT_MENU_URL)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"

    def __str__(self):
        return self.name


# class MenuItem(models.Model):
#     parent = models.ForeignKey("self", blank=True, null=True, related_name="children", on_delete=models.CASCADE)
#     menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
#
#     position = models.PositiveIntegerField(default=1, verbose_name="Item position")
#     depth = models.PositiveIntegerField(default=0, verbose_name="Item depth")
#     name = models.CharField(max_length=50, verbose_name="Item name")
#     slug = models.SlugField(max_length=50, unique=True, verbose_name="Item slug name")
#
#     class Meta:
#         verbose_name = "Menu item"
#         verbose_name_plural = "Menu items"
#
#     def __str__(self):
#         return self.name

class MenuItem(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children", on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)

    name = models.CharField(max_length=50, verbose_name="Item name")
    depth = models.PositiveIntegerField(default=0, verbose_name="Item depth")
    url = models.URLField(default=settings.DEFAULT_MENU_URL)

    class Meta:
        verbose_name = "Menu item"
        verbose_name_plural = "Menu items"

    def __str__(self):
        return self.name
