from django.contrib import admin

from .models import Category, Place


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'registered']