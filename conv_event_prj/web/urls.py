from . import views
from django.urls import path


urlpatterns = [
    path('<str:store>/', views.product, name="index"),
    path('<str:store>/<int:pk>/', views.detail, name="detail"),
    path('<str:store>/<int:pk>/like/', views.like_post, name="like"),

    path('<str:store>/<int:pk>/new_comment/', views.new_comment, name="new_comment"),
]