from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCommentCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('<int:pk>/comment/', ProductCommentCreateView.as_view(), name='product_comment'),
]