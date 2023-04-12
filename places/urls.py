from django.urls import path

from . import views

urlpatterns = [
    path('lugares/', views.PlaceListView.as_view(), name='place_list'),
    path('lugares/<int:pk>/', views.PlaceDetailView.as_view(), name='place_detail'),
    path('lugares/<int:pk>/atualizar/', views.PlaceUpdateView.as_view(), name='place_update'),
    path('lugares/adicionar/', views.PlaceCreateView.as_view(), name='place_create'),
]
