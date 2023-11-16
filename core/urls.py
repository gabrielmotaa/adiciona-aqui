from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(_("about-us/"), views.AboutUsView.as_view(), name="about_us"),
]
