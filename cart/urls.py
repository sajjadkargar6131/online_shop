from django.urls import path
from .views import cart_detail_view, test

urlpatterns = [
    path('', cart_detail_view, name='cart_detail'),
    path('test/', test, ),
]