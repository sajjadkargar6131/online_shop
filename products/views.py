from django.shortcuts import render
from django.views import generic
from .models import Product

class ProductListView(generic.ListView):

    template_name = 'products/product_list.html'
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'
    
class ProductDetailView(generic.DetailView):
    
    template_name = 'products/product_detail.html'
    queryset = Product.objects.filter(active=True)
    context_object_name = 'product'