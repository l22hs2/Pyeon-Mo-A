from web import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('event/', include("web.urls")),

    path('accounts/', include('allauth.urls'), name="google"), 
]
