from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'core/home.html'


class AboutUsView(TemplateView):
    template_name = 'core/about_us.html'
