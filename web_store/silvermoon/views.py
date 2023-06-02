from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .utils import *
from .serializers import GameCartSerializer
from .filters import GameFilter
from urllib.parse import urlencode

# def shop_page(request):
#     game_filter = GameFilter(request.GET, queryset=Game.objects.all())
#     context = {
#          'form': game_filter.form,
#          "Games": game_filter.qs
# 	}
#     return render(request, "silvermoon/shop_page.html", context)

def shop_page(request):
    queryset = Game.objects.all()
    existing_params = request.GET.copy()
    if 'sort_by' in request.GET:
          category = request.GET['sort_by']
          if category is not '':
                 queryset = queryset.order_by(category)
    filtered_url = request.path + '?' + urlencode(existing_params)
    
    context = {
        "Games": queryset,
        "Genres": Genre.objects.all(),
        "Subgenres": Subgenre.objects.all(),
        "Visuals": Visual.objects.all(),
		"Themes": Theme.objects.all(),
        "Features": Feature.objects.all(),
        "Players": PlayersType.objects.all(),
	}
    return render(request, "silvermoon/shop_page.html", context)

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