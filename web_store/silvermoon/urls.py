from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_page, name='shop_page'),
    path('cart/', views.cart, name='cart'),
    path('cart-data/', views.cart_data, name='cart-data'),
]
