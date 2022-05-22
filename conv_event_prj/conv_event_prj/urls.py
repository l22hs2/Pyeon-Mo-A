from web import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product),
    path('sample', views.sample),
    # path('web/', include('web.urls')),
]
