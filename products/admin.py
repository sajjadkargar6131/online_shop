from django.contrib import admin
from .models import Product, Comment

class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'active', ]
    extra = 0
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', ]
    inlines = [
        CommentsInline,
    ]
    
    
    
@admin.register(Comment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'body', 'active', ]