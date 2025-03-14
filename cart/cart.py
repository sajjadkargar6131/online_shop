from products.models import Product

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')


        if not isinstance(cart, dict):
            self.session['cart'] = {}
            cart = self.session['cart']

        self.cart = cart.copy() 

    def add_to_cart(self, product, quantity=1):
        
        product_id = str(product.id)
        
        if product_id not in self.cart :
            
            self.cart[product_id] = {'quantity' : quantity}
        
        else :
            
            self.cart[product_id]['quantity']+= quantity
            
        self.save()
        
    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
            
    def remove_from_cart(self, product):
        
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save() 

    def __iter__(self):
        
        product_ids = self.cart.keys()
        
        products = Product.objects.filter(id__in=product_ids)
        
        cart = self.cart.copy()                   
        
        for product in products :
            
            cart[str(product.id)]['product_obj'] = product
            
        for item in cart.values():
            yield item
    
    def __len__(self) :
        return len(self.cart.keys())
    
    def clear(self):
        del self.session['cart']
        self.save()
        
    def total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return sum(product.price for product in products )        