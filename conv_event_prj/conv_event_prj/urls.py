from web import views
from django.contrib import admin
from django.urls import include, path

app_name = 'posts'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product, name="index"),
    path('sample', views.sample),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:post_id>/like/', views.like_post, name="like_post"),
]
