from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .utils import *
from .serializers import GameCartSerializer

def shop_page(request):
    return render(request, "silvermoon/shop_page.html", {
        "Games": Game.objects.all()
    })

def cart(request):
    return render(request, "silvermoon/cart.html")

# def cart(request):
# 	data = cartData(request)

# 	cartItems = data['cartItems']
# 	order = data['order']
# 	items = data['items']

# 	context = {'items':items, 'order':order, 'cartItems':cartItems}
# 	return render(request, 'silvermoon/cart.html', context)

@api_view(['GET'])
def cart_data(request):
      games =  Game.objects.all()
      serializer = GameCartSerializer(games, many=True)
      return Response(serializer.data)