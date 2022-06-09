from django.contrib import admin
from web.models import Cu, Gs25, Seven, Cu_comment, Gs25_comment, Seven_comment

# Register your models here.
admin.site.register(Cu)
admin.site.register(Gs25)
admin.site.register(Seven)

admin.site.register(Cu_comment)
admin.site.register(Gs25_comment)
admin.site.register(Seven_comment)