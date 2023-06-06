import json
import random
from .models import *

def genKey():
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4',
           '5', '6', '7', '8', '9']
    x = 0
    newKey = ""
    while x < 17:
        digit = random.randint(0, 34)
        if x == 5 or x == 11:
            newKey += '-'
        else:
            newKey += symbols[digit]
        x += 1
    return newKey

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
					'get_total':total,
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
