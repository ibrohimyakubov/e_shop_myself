from django.contrib import admin

from basic.models import Setting, Category, Product

admin.site.register([Setting, Category, Product])
