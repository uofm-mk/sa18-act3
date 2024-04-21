from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})

def show(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'myapp/show.html', {'product': product})
