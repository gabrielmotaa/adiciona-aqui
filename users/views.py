from django.contrib.auth import views
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


class LoginView(views.LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(views.LogoutView):
    pass


class PasswordResetView(views.PasswordResetView):
    template_name = 'users/password_reset.html' 


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = 'users/password_confirm.html'
