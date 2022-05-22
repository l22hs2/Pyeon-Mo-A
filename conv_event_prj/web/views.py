from django.shortcuts import render

# Create your views here.

def product(request):
    return render(request, 'web/product.html')
    
def sample(request):
    return render(request, 'web/sample.html')