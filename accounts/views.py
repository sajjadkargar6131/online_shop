from django.views.generic import CreateView
from .forms import CustomUserCreatinForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    
        form_class = CustomUserCreatinForm
        template_name = 'registration/signup.html'
        success_url = reverse_lazy('login')