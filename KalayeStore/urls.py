from django.contrib import admin
from django.urls import path, include
from KalayeStore.views import index
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('KalayeStore.urls')),
    path('detail/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('shop/', views.shop, name='shop'),
]
