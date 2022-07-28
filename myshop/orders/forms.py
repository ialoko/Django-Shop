from operator import truediv
from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid']
        widgets = {'paid': forms.HiddenInput()}
    