from django import forms
from .models import ProductComment

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['body', 'star']
        labels = {
            'body' : 'متن',
            'star' : 'امتیاز'
        }