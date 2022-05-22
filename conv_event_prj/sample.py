import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conv_event_prj.settings')
import django
django.setup()
from web.models import Product

a = Product.objects.filter(name="컬러송이토마토(500G/팩)")
print(bool(a))