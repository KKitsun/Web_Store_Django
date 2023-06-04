from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_page, name='shop_page'),
    path('cart/', views.cart, name='cart'),
    path('cart-data/', views.cart_data, name='cart-data'),
    path('checkout/', views.checkout_page, name='checkout'),
    path('game/<int:id>', views.game_page, name='game_page'),
    path('process-payment-result/', views.processPaymentResult, name='process-payment-result'),
]
