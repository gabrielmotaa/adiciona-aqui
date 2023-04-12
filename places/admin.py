from django.contrib import admin

from .models import Category, Place


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class CategoryInline(admin.TabularInline):
    model = Place.categories.through
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'registered']
    list_filter = ['registered']
    inlines = [CategoryInline]
