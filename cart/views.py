from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from products.models import Product
from .forms import AddToCartForm

def cart_detail_view(request):
    cart = Cart(request) 
    for item in cart :
        item['product_item_quantity'] = AddToCartForm(initial={
            'quantity': item['quantity'],
            'inplace' : True,
        })
    return render(request, 'cart/cart.html',{
        'cart' : cart,
    })

@require_POST   
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add_to_cart(product, quantity, replace=cleaned_data['inplace'])
    return redirect('cart:cart_detail')

def remove_from_cart_view(request, product_id):
     cart = Cart(request)
     product = get_object_or_404(Product, id=product_id)
     cart.remove_from_cart(product)
     return redirect('cart:cart_detail')
 
 
def empty_cart_view(request):
     cart = Cart(request)
     cart.empty()
     return redirect('cart:cart_detail')
        
    
    
    
def test(request):
    response = request.method
    response2 = request.path
    id = request.GET.get('id', 'id not selected')
    response3 = request.get_full_path()
    response4 = request.build_absolute_uri()
    response5 = request.META['REMOTE_ADDR']
    response6 = request.META.get('HTTP_USER_AGENT')
    return render(request, 'cart/test.html', context={
        'data': {
            'request.method':[response,],
            'request.path':[response2],
            'request.get_full_path()':[response3],
            'request.build_absolute_uri()':[response4],
            'request.META["REMOTE_ADDR"]':[response5],
            ' request.META.get("HTTP_USER_AGENT")':[response6],
            
        }
    })