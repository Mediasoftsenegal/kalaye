from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from KalayeStore.views import index, detail,contact,cart,checkout,shop

urlpatterns = [
   
   path('', index,name='index'),
   path('detail/', detail, name='detail'),
   path('contact/', contact, name='contact'),
   path('cart/',cart, name='cart'),
   path('checkout/', checkout, name='checkout'),
   path('shop/', shop, name='shop'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
