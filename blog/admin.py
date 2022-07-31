import imp
from django.contrib import admin
from .models import Contact,Blog,FAQ
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(FAQ)