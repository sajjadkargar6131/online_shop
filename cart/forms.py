from django import forms

class AddToCart(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1,30)]
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)