from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied

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
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        qs = qs.order_by('-pk')
        return qs

class PlaceCreateView(LoginRequiredMixin, CreateView):
    model = Place
    template_name = 'places/place_create.html'
    form_class = PlaceForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('categories')


class PlaceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Place
    template_name = 'places/place_update.html'
    form_class = PlaceForm

    def test_func(self):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return True
