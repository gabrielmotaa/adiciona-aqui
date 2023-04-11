from django.urls import path

from . import views

urlpatterns = [
    path('categorias/', views.CategoryListView.as_view(), name='category_list'),
    path('categorias/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('lugares/', views.PlaceListView.as_view(), name='place_list'),
    path('lugares/<int:pk>', views.PlaceDetailView.as_view(), name='place_detail'),
    path('lugares/adicionar/', views.PlaceCreateView.as_view(), name='place_create'),
]
