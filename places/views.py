from django.views.generic import ListView, DetailView, CreateView

from .models import Place, Category
from .forms import PlaceForm


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'places/category_detail.html'
    context_object_name = 'category'


class CategoryListView(ListView):
    model = Category
    template_name = 'places/category_list.html'
    context_object_name = 'categories'


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'places/place_detail.html'
    context_object_name = 'place'


class PlaceListView(ListView):
    model = Place
    template_name = 'places/place_list.html'
    context_object_name = 'places'


class PlaceCreateView(CreateView):
    model = Place
    template_name = 'places/place_create.html'
    form_class = PlaceForm
