from django.shortcuts import get_object_or_404, redirect, render
from .models import Product
from django.db.models import Count

# Create your views here.

def product(request):
    products = Product.objects.all()
    best = Product.objects.all().annotate(count=Count('like_users')).order_by('-count')[:1]
    # products = products.annotate(count=Count('like_users')).order_by('-count')
    return render(request, 'web/product.html',
        {
            'products': products,
            'best': best,
        }    
    )
    
def detail(request, pk):
    products = Product.objects.get(pk=pk)
    return render(request, 'web/detail.html',
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


# def like_post(request, post_id):
#     post = get_object_or_404(Product, id=post_id)
#     if request.user in post.like_users.all():
#         post.like_users.remove(request.user)
#     else:
#         post.like_users.add(request.user)

def like_post(request, post_id):
    if request.user.is_authenticated:
        article = get_object_or_404(Product, pk=post_id)

        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('detail', post_id)
    return redirect('detail')