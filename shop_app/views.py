from django.shortcuts import render
from .models import Product
from django.http import HttpResponse, Http404

# Create your views here.

def render_product(request, product):
	return render(request, 'product.html', { 'product': product, })

def product_view(request, slug):
	product = Product.objects.filter(slug=slug).first()
	if not product:
		raise Http404("Product does not exist")
	request.toolbar.set_object(product)
	return render_product(request, product)

