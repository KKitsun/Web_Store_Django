from django.shortcuts import render, redirect, HttpResponse
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
    if 'game_title' in request.GET:
          title = request.GET['game_title']
          if title != '':
                 queryset = queryset.filter(title__icontains=title)
    if 'genre' in request.GET:
          id = request.GET['genre']
          if id != '':
                 queryset = queryset.filter(genre__id=id)
    if 'subgenre' in request.GET:
          id = request.GET['subgenre']
          if id != '':
                 queryset = queryset.filter(subgenre__id=id)
    if 'visual' in request.GET:
          id = request.GET['visual']
          if id != '':
                 queryset = queryset.filter(visual__id=id)
    if 'theme' in request.GET:
          id = request.GET['theme']
          if id != '':
                 queryset = queryset.filter(theme__id=id)
    if 'feature' in request.GET:
          id = request.GET['feature']
          if id != '':
                 queryset = queryset.filter(feature__id=id)
    if 'playerType' in request.GET:
          id = request.GET['playerType']
          if id != '':
                 queryset = queryset.filter(playersType__id=id)

    if 'sort_by' in request.GET:
          category = request.GET['sort_by']
          if category != '':
                 queryset = queryset.order_by(category)
    
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

def checkout_page(request):
    data = cookieCart(request)
    order = data['order']
    items = data['items']
    context = {'items':items, 'order':order}
    return render(request, "silvermoon/checkout.html", context)

def game_page(request, id):
    game = Game.objects.get(pk=id)
    context = {'game':game}
    return render(request, "silvermoon/game_page.html", context)

@api_view(['GET'])
def cart_data(request):
      games =  Game.objects.all()
      serializer = GameCartSerializer(games, many=True)
      return Response(serializer.data)
    