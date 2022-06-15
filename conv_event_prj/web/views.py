from django.shortcuts import get_object_or_404, redirect, render

from .models import Product, Comment
from django.db.models import Count

from .forms import CommentForm
from django.core.exceptions import PermissionDenied

# Create your views here.

def home(request):
    return render(request, 'web/home.html',
        {
            'cu': Product.objects.filter(store="CU").annotate(count=Count('like_users')).order_by('-count')[:3],
            'gs25': Product.objects.filter(store="GS25").annotate(count=Count('like_users')).order_by('-count')[:3],
            'seven': Product.objects.filter(store="Seven").annotate(count=Count('like_users')).order_by('-count')[:3],
            'recent_comment': Comment.objects.all().order_by('-created_at')[:5]
        }
    )

def product(request, store):
    products = Product.objects.filter(store=store)
    sort = request.GET.get('sort','')
    
    if sort:
        if sort == 'price_low':
            products = products.order_by('price')
        elif sort == 'price_high':
            products = products.order_by('-price')
        elif sort == 'like':
            products = products.annotate(count=Count('like_users')).order_by('-count')

    return render(request, 'web/product.html',
        {
            'products': products,
            'count': products.count(),
            'store': store,
        }    
    )
    
def detail(request, pk, store):
    products = get_object_or_404(Product, pk=pk)
    return render(request, 'web/detail.html',
        {
            'products': products,
            'store': store,
            'comment_form': CommentForm,
            'comment_count' : Comment.objects.filter(product=pk).count(),
        }    
    )

def like(request, pk, store):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk = pk)

        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect('detail', store, pk)
    return redirect("/accounts/login/")

def new_comment(request, pk, store):
    if request.user.is_authenticated:
        post = get_object_or_404(Product, pk=pk)

        if request.method == "POST":

            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.product = post
                comment.author = request.user
                comment.save()
                return redirect('detail', store, pk)
            else:
                return redirect('detail', store, pk)
        else:
            raise PermissionDenied

def delete_comment(request, pk, store, pks):
    comment = get_object_or_404(Comment, pk=pks)
    # product = comment.product
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect('detail', store, pk)
    else:
        raise PermissionDenied


def search(request):
    products = Product.objects.all()

    q = request.POST.get('q', "")

    products = products.filter(name__icontains=q)

    return render(request, 'web/product.html',
        {
            'products': products,
            'count': products.count(),
            'isSearch': True,
            'q': q,
        }    
    )