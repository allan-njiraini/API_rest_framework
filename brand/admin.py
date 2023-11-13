from django.contrib import admin
from brand.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "image"]


admin.site.register(Product, ProductAdmin)