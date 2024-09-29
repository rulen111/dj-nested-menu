from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "url"]
    readonly_fields = ["id", "url"]
    ordering = ["name", "url"]

    def save_model(self, request, obj, form, change):
        """
        Redefining save_model method for autocompletion of "url" field
        """
        super().save_model(request, obj, form, change)
        obj.url = obj.url + obj.name + str(obj.pk)
        obj.save()


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["id", "parent", "menu", "name", "sort", "url"]
    readonly_fields = ["id", "url"]
    ordering = ["menu", "parent", "-sort", "name"]

    def save_model(self, request, obj, form, change):
        """
        Redefining save_model method for autocompletion of "url" field
        """
        super().save_model(request, obj, form, change)
        obj.url = obj.menu.url + str(obj.pk)
        obj.save()
