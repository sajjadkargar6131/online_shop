from django.shortcuts import get_object_or_404
from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages



from .models import Product, Comment
from .forms import ProductCommentForm

class ProductListView(generic.ListView):

    template_name = 'products/product_list.html'
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'
    
    
class ProductDetailView(generic.DetailView):
    
    template_name = 'products/product_detail.html'
    queryset = Product.objects.filter(active=True)
    context_object_name = 'product'
    form_class = ProductCommentForm
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(active=True)
        context['comments_count'] = context['comments'].count()
        context['form'] = ProductCommentForm
        return context
    
    
class ProductCommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = ProductCommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.product = get_object_or_404(Product, pk=self.kwargs["pk"])
        comment.author = self.request.user
        comment.save()
        messages.success(self.request, 'نظر شما با موفقیت ثبت شد')
        return JsonResponse({"message": "Comment added successfully", "status": "success"})

    def form_invalid(self, form):
        messages.error(self.request, 'مشکلی در ثبت کامنت بوجود آمد')
        return JsonResponse({"message": "Error submitting comment", "status": "error", "errors": form.errors})