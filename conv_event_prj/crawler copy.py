

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conv_event_prj.settings')
import django
django.setup()
from web.models import product


if __name__=='__main__':
    product(name='3', price='1', image='1').save()
