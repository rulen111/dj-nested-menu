from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "url"]
    readonly_fields = ["id", "url"]
    ordering = ["name", "url"]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # obj.slug = obj.name + str(obj.pk)
        obj.url = obj.url + obj.name + str(obj.pk)
        obj.save()


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["id", "parent", "menu", "name", "depth", "url"]
    readonly_fields = ["id", "depth", "url"]
    ordering = ["depth", "name"]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.parent:
            obj.depth = obj.parent.depth + 1
        obj.url = obj.menu.url + str(obj.pk)
        obj.save()
