from django import forms
from .models import Comment

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'star']
        labels = {
            'body' : 'متن',
            'star' : 'امتیاز'
        }