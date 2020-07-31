from django.shortcuts import render

# Create your views here.
from .models import *
def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request,'store/store.html',context)


def cart(request):	
	order_items = OrderItem.objects.all()
	order,Created = Order.objects.get_or_create(complete=False)
	context = {'order_items':order_items,'order':order}
	return render(request,'store/cart.html',context)


def checkout(request):
	items = OrderItem.objects.all()
	order,Created = Order.objects.get_or_create(complete=False)
	context = {'items':items,'order':order}
	return render(request,'store/checkout.html',context)

def UpdateItem(request):
	context = {}
	return render(request,'store/checkout.html',context)

def search(request):
	book_name = request.GET.get('search')
	# print(book_name)
	products = Product.objects.filter(name__icontains=book_name)
	# products = Product.objects.filter(Productname_icontains=book_name)
	context = {'products':products}
	# context = {}
	print(products)
	return render(request,'store/search.html',context)