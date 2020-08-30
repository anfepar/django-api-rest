from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from products.models import Product, Color, Size, Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'picture', 'category', 'description','created', 'modified' )

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'ref' )    

@admin.register(Size)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name' )    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'icon' )    