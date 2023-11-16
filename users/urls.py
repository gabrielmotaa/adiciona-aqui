from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
    path(_("signup/"), views.SignupView.as_view(), name="signup"),
    path(_("login/"), views.LoginView.as_view(), name="login"),
    path(_("logout/"), views.LogoutView.as_view(), name="logout"),
    path(
        _("password-reset/"), views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        _("password-reset/done/"),
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        _("reset/<uidb64>/<token>/"),
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        _("reset/done/"),
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
