from os import environ
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Cu, Gs25, Seven
from django.db.models import Count
from django.contrib import messages

from .forms import Cu_CommentForm, Gs25_CommentForm, Seven_CommentForm
from django.core.exceptions import PermissionDenied

# Create your views here.

def home(request):
    return render(request, 'web/home.html',
        {
            'cu': Cu.objects.all().annotate(count=Count('like_users')).order_by('-count')[:3],
            'gs25': Gs25.objects.all().annotate(count=Count('like_users')).order_by('-count')[:3],
            'seven': Seven.objects.all().annotate(count=Count('like_users')).order_by('-count')[:3],
        }
    )

def setStore(store):
    if store == "gs25":
        dbName = Gs25
    elif store == "cu":
        dbName = Cu
    elif store == "seven":
        dbName = Seven

    return dbName

def setFrom(store):
    if store == "gs25":
        CommentForm = Gs25_CommentForm
    elif store == "cu":
        CommentForm = Cu_CommentForm
    elif store == "seven":
        CommentForm = Seven_CommentForm
    
    return CommentForm

def product(request, store):
    dbName = setStore(store)

    products = dbName.objects.all()
    best = dbName.objects.all().annotate(count=Count('like_users')).order_by('-count')[:3]
    # products = products.annotate(count=Count('like_users')).order_by('-count')
    return render(request, 'web/product.html',
        {
            'products': products,
            'best': best,
            'store': store,
        }    
    )
    
def detail(request, pk, store):
    dbName = setStore(store)

    products = get_object_or_404(dbName, pk=pk)
    return render(request, 'web/detail.html',
        {
            'products': products,
            'store': store,
            'comment_form': setFrom(store),
        }    
    )

def like_post(request, pk, store):
    dbName = setStore(store)

    if request.user.is_authenticated:
        product = get_object_or_404(dbName, pk = pk)

        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect('detail', store, pk)
    messages.warning(request, '로그인이 필요한 작업입니다')
    return redirect('detail', store, pk)

def new_comment(request, pk, store):
    dbName = setStore(store)

    if request.user.is_authenticated:
        post = get_object_or_404(dbName, pk=pk)

        if request.method == "POST":

            comment_form = setFrom(store)(request.POST)
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