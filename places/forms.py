from django import forms

from .models import Category, Place


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ['name', 'address', 'phone', 'site', 'registered', 'user', 'categories', 'image']
