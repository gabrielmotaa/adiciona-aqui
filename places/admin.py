from django.contrib import admin

from parler.admin import TranslatableAdmin

from .models import Category, Place


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    pass


class CategoryInline(admin.TabularInline):
    model = Place.categories.through
    extra = 0


@admin.action(description='Marcar lugares como registrados')
def make_registered(modeladmin, request, queryset):
    queryset.update(registered=True)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'registered']
    list_filter = ['registered']
    inlines = [CategoryInline]
    actions = [make_registered]

