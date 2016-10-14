from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest,HttpResponsePermanentRedirect,HttpResponseForbidden
import json
from models import *


MENU = {
	'1':
		[
			{'name':'Beer','id':1,'price':130},
			{'name':'Chocolate','id':2,'price':30},
			{'name':'Lay\'s','id':3,'price':10},
			{'name':'Butter Chkn','id':4,'price':230},
			{'name':'Tawa Chkn','id':5,'price':230},
			{'name':'Tawa Roti','id':6,'price':30},
			{'name':'Butter Roti','id':7,'price':10},
			{'name':'Naan','id':8,'price':40},
			{'name':'Rice','id':9,'price':180},
			{'name':'Noodles','id':10,'price':130},
			{'name':'Haka Noodles','id':11,'price':150},
			{'name':'Ice Cream','id':12,'price':20},
			{'name':'Tea','id':13,'price':10}
		],
	'2':
		[
			{'name':'Item1','id':4,'price':30},
			{'name':'Item2','id':5,'price':30},
			{'name':'Item3','id':6,'price':30}
		]
}

def test(request):
	return HttpResponse('HAHAHAHAHAHAHAHAHAHA',content_type='application/json')

def  get_menu(request,hotelid):
	return HttpResponse(json.dumps(MENU[hotelid]),content_type='application/json')

@csrf_exempt
def place_order(request,FMN):
	resp = {'success':False, 'grandtotal':0}
	try:
		try:
			orders = request.POST.get('order',[])
			if not orders:
				raise
			orders = json.loads(orders)
		except:
			body = json.loads(request.body)
			orders = body.get('order',[]) if body else []
		grandtotal = 0
		for order in orders:
			if int(order['units']):
				o = Orders(bookingId=FMN,itemId=order['id'],unit=order['units'],price=order['price'])
				o.save()
				grandtotal += (int(order['price']) * int(order['units']))
		resp = {'success':True,'grandtotal':grandtotal}
	except:
		raise
	return HttpResponse(json.dumps(resp),content_type='application/json')

def get_order(request,FMN):
	resp = {'success':False,'order':[],'grandtotal':0}
	try:
		orders = []
		grandtotal = 0
		o = Orders.objects.filter(bookingId=FMN)
		for order in o:
			orders.append({'id':order.itemId,'price':order.price,'unit':order.unit,'total':(order.price*order.unit)})
			grandtotal += (order.price*order.unit)
		resp = {'success':True,'order':orders,'grandtotal':grandtotal}
	except:
		raise
	return HttpResponse(json.dumps(resp),content_type='application/json')
