# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('list_produit', views.List_produit, name='list_produit'),
    path('produit/<int:produit_id>/', views.detail_produit, name='detail_produit'),
    path('panier', views.panier, name='panier'),
]
