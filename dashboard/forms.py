from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm): # for admin
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity','cost_per_item']

class OrderForm(forms.ModelForm):  # for staff
    class Meta:
        model = Order
        fields = ['product','order_quantity']
