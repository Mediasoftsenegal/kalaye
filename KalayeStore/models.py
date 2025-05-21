from django.db import models

# Create your models here.
"""
Product Model
-name
-price
-description
-image
-stock
"""

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
    
"""
User Model
-username 
-password
-email
-phone
-address_livraison
"""    
    
class User_db(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=15)
    address_livraison = models.TextField()

    def __str__(self):
        return self.username