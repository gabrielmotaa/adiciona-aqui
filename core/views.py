from django.views.generic import TemplateView

from places.models import Place


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["places"] = Place.objects.all().order_by("-created_at")[:3]
        return context


class AboutUsView(TemplateView):
    template_name = "core/about_us.html"
