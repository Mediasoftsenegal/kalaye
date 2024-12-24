from django.contrib import admin
from .models import Categorie, Produit, Panier

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Panier)
