from django.shortcuts import render
from .models import Product
from django.http import HttpResponse, Http404

# Create your views here.
def render_product(request, slug):
	product = Product.objects.filter(slug=slug).first()
	if not product:
		raise Http404("Product does not exist")	
	return render(request, 'product.html', { 'product': product, })