from django.urls import path

from . import views

urlpatterns = [
    path('locais/', views.PlaceListView.as_view(), name='place_list'),
    path('locais/<int:pk>/', views.PlaceDetailView.as_view(), name='place_detail'),
    path('locais/<int:pk>/atualizar/', views.PlaceUpdateView.as_view(), name='place_update'),
    path('locais/adicionar/', views.PlaceCreateView.as_view(), name='place_create'),
]
