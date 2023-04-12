from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Place
from .forms import PlaceForm


class PlaceDetailView(LoginRequiredMixin, DetailView):
    model = Place
    template_name = 'places/place_detail.html'
    context_object_name = 'place'


class PlaceListView(LoginRequiredMixin, ListView):
    model = Place
    template_name = 'places/place_list.html'
    context_object_name = 'places'


class PlaceCreateView(LoginRequiredMixin, CreateView):
    model = Place
    template_name = 'places/place_create.html'
    form_class = PlaceForm


class PlaceUpdateView(LoginRequiredMixin, UpdateView):
    model = Place
    template_name = 'places/place_update.html'
    form_class = PlaceForm
