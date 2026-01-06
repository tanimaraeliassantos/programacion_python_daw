from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'cantidad']
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                   'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
                   'cantidad': forms.NumberInput(attrs={'class': 'form-control'})}
