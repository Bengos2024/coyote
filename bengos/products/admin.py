from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=['code','name']
admin.site.register(Product,ProductAdmin)