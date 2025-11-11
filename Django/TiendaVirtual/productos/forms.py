from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio',
                  'stock', 'disponible', 'categoria']
        widgets = {'descripcion': forms.Textarea(attrs={'rows': 4})}
