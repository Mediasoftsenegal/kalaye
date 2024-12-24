from django.shortcuts import render, get_object_or_404
from store.models import  Produit, Panier

# Create your views here.
def list_produit(request) :
    produits = Produit.objects.all()
    return render (request,'store/produit_list.html', {'produits':produits})

def produit_detail(request, produit_id) :
    produit= get_object_or_404(Produit,id=produit_id)
    return render(request, 'store/produit_detail.html', {'produit' : produit})

def panier(request): 
    produit_panier = Panier.Objects.all()
    total = sum(item.montant() for item in produit_panier)
    return render(request, 'store/panier.html', {'produit_panier' : produit_panier, 'total' : total})