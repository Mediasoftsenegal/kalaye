from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nom_categorie

class Produit(models.Model): 
    nom_produit = models.CharField(max_length=200)
    descri_produit = models.TextField()
    prix = models.DecimalField(max_digits=10,decimal_places=0)
    stock = models.PositiveIntegerField()
    nom_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='produits/')
    
    def __str__(self): 
        return self.nom_produit
    
class Panier(models.Model): 
    nom_produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.quantite} of {self.nom_produit}"
    
    def montant_total(self):
        return self.Produit.prix * self.quantite