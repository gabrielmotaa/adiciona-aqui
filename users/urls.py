from django.urls import path

from . import views

urlpatterns = [
    path('registrar/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('redefinir-senha/', views.PasswordResetView.as_view(), name='password_reset'),
    path('redefinir-senha/pronto/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('redefinir/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('redefinir/pronto/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
