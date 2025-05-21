from django.contrib import admin

# Register your models here.
from KalayeStore.models import Product, User_db

admin.site.register(Product)
admin.site.register(User_db)
