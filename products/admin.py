from django.contrib import admin
from .models import Product, ProductComment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', ]
    
    
@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    pass