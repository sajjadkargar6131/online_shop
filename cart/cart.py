from products.models import Product
from django.contrib import messages
from django.utils.translation import gettext as _

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')


        if not isinstance(cart, dict):
            self.session['cart'] = {}
            cart = self.session['cart']

        self.cart = cart.copy() 

    def add_to_cart(self, product, quantity=1, replace=False):
        
        product_id = str(product.id)
        
        if product_id not in self.cart :
            
            self.cart[product_id] = {'quantity' : 0}
        
        if replace :
            
             self.cart[product_id]['quantity'] = quantity
             
        else :
            
            self.cart[product_id]['quantity'] += quantity
        
        messages.success(self.request, _('Product successfully added to Cart'))
            
        self.save()
        
    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
            
    def remove_from_cart(self, product):
        
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request, _('Product successfully removed from Cart'))
            self.save() 

    def __iter__(self):
        
        product_ids = self.cart.keys()
        
        products = Product.objects.filter(id__in=product_ids)
        
        cart = self.cart.copy()                   
        
        for product in products :
            
            cart[str(product.id)]['product_obj'] = product
            
        for item in cart.values():
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item
    
    def __len__(self) :
        return sum(item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session['cart']
        self.save()
        
    def total_price(self):
        
        return sum(item['quantity'] * item['product_obj'].price for item in self.cart.values())        



# class Cart:
#     def __init__(self, request) :
#         self.request = request
#         self.session = request.session
#         self.cart = request.session.setdefault('cart',{})
        
#     def add_to_cart(self, product, quantity=1):
        
#         product_id = str(product.id)
        
#         if product.stock < quantity :
#             quantity = product.stock
            
#         if product.id not in self.cart:
#             self.cart[product_id] = {'quantity' : quantity}
#         else :
#             self.cart[product_id]['quantity'] += quantity
            
#         self.save()
        
#     def remove_from_cart(self, product, decrease_quantity=False):
        
#         product_id = product.id
        
#         if product_id not in self.cart :
#             if decrease_quantity and self.cart[product_id]['quantity']>1:
#                 self.cart[product_id]['quantity'] -= 1
#             else :
#                 del self.cart[product_id]
#             self.save()
    
#     def save(self):
#         self.session.modified = True
        
#     def __iter__(self):
        
#         product_ids = self.cart.keys()
#         products = Product.objects.filter(id__in=product_ids)
#         cart = self.cart.copy()
        
#         for product in products :
#             cart[str(product.id)]['product_obj']= product
#             cart[str(product.id)]['price'] = product.price
            
#         for item in cart.values():
#             yield item
    
#     def __len__(self):
#         return sum(item['quantity'] for item in self.cart.values())
    
#     def clear(self):
#         self.session.pop('cart', None)
#         self.save()
        
#     def total_price(self):
#         product_ids = self.cart.keys()
#         products = Product.objects.filter(id__in=product_ids)
#         total = 0
#         for product in products :
#             product_id = str(product.id)
#             quantity = self.cart[product_id]['quantity']
#             total += product.price * quantity
#         return total
        
    