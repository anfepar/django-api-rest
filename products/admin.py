from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from products.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'picture', 'category', 'description','created', 'modified' )