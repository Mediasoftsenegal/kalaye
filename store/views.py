from django.shortcuts import render, get_object_or_404
from .models import Produit, Panier

# Create your views here.
def index(request):
    produits =Produit.objects.all()
    return render (request,'store/index.html',{'produit': produits})

def List_produit(request):
    produits =Produit.objects.all()
    return render (request,'store/list_produit.html',{'produit': produits})


def detail_produit(request,produit_id): 
    produit = get_object_or_404(Produit,id=produit_id)
    return render (request,'store/detail_produit.html', {'produit': produit})

def panier(request):
    panier_item = panier.objects.all()
    total = sum(item.Produit.prix() for item in panier_item)
    return render(request, 'store/panier/html', {'panier': panier, 'total': total})
