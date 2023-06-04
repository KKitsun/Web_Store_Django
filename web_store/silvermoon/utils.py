import json
from .models import *

def cookieCart(request):
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}

	items = []
	order = {'get_cart_total':0, 'get_cart_items':0}

	for i in cart:
		try:	
			if(cart[i]['quantity'] > 0):  

				product = Game.objects.get(id=i)
				total = (product.price * cart[i]['quantity'])

				order['get_cart_total'] += total
				order['get_cart_items'] += cart[i]['quantity']

				item = {
					'product':{
						'id':product.id,
						'name':product.title, 
						'price':product.price, 
						'imageURL':product.image.url
						}, 
					'quantity':cart[i]['quantity'],
					'get_total':total
				}
				items.append(item)

		except:
			pass
			
	return {'order':order, 'items':items}

	
def guestOrder(request, data):
	name = data['paymentData']['email'].split('@')[0]
	email = data['paymentData']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	order = Order.objects.create(
		email = email,
		name = name,
	)

	for item in items:
		game = Game.objects.get(id=item['product']['id'])
		orderGame = OrderGame.objects.create(
			order=order,
			game=game,
			quantity=(item['quantity'] if item['quantity']>0 else -1*item['quantity']),
		)
	return order
