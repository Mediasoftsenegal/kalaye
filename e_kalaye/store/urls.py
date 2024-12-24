from django.urls import path 
from . import views

urlpatterns = [
    path('', views.list_produit, name='produit_list'),
    path('produits/<int:produit_id>/', views.produit_detail, name ='produit_detail'),
    path('panier/',views.panier, name='panier'),
]

