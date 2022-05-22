from django.shortcuts import render
from .models import Product

# Create your views here.

def product(request):
    products = Product.objects.all()
    return render(request, 'web/product.html',
        {
            'products': products,
        }    
    )
    
def sample(request):
    products = Product.objects.all()
    return render(request, 'web/sample.html',
        {
            'products': products,
        }    
    )