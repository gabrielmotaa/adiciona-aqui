from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
    path(_("places/"), views.PlaceListView.as_view(), name="place_list"),
    path(_("places/<int:pk>/"), views.PlaceDetailView.as_view(), name="place_detail"),
    path(
        _("places/<int:pk>/update/"),
        views.PlaceUpdateView.as_view(),
        name="place_update",
    ),
    path(_("places/add/"), views.PlaceCreateView.as_view(), name="place_create"),
]
