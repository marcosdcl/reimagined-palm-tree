from product.models import Product
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


admin.site.register(Product, ProductAdmin)
