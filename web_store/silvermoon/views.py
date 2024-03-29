from django.shortcuts import render, redirect, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .utils import *
from .serializers import GameCartSerializer
import json
from django.http import JsonResponse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

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

def pdf_report_create(request, order):
    data = cookieCart(request)
    order_details = data['order']
    items = data['items']
    game_keys = []
    for k in range(order_details['get_cart_items']):
          game_keys.append(genKey())

    print(game_keys)
    template_path = 'silvermoon/Invoice_template_for_pdf.html'

    context = {'items':items, 'order':order_details, 'specific_order': order, 'game_keys':game_keys}

    template = get_template(template_path)

    html = template.render(context)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    pdf = result.getvalue()
    
    to_emails = [str(order.email)]
    subject = "Silvermoon замовлення"
    email = EmailMessage(subject, body="Дякуємо за покупку!", from_email=settings.EMAIL_HOST_USER, to=to_emails)
    email.attach("Silvermoon_invoice.pdf", pdf, "application/pdf")
    email.send(fail_silently=False)

def processPaymentResult(request):
    paymentResult = json.loads(request.body)
    order = guestOrder(request, paymentResult)
    order.status = Order.COMPLETED
    order.save()
    pdf_report_create(request, order)
    return JsonResponse('Successful transaction', safe=False)

@api_view(['GET'])
def cart_data(request):
      games =  Game.objects.all()
      serializer = GameCartSerializer(games, many=True)
      return Response(serializer.data)
    