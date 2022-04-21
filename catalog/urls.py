from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_home, name='catalog_home'),
    path('create', views.create, name='create'),
    path('/<int:pk>/', views.CatalogDetailView.as_view(), name='catalog_detail'),
    path('/<int:pk>/update', views.CatalogUpdateView.as_view(), name='catalog_update'),
    path('/<int:pk>/delete', views.CatalogDeleteView.as_view(), name='catalog_delete'),
]
