from django import forms
from .models import Libro
from django.forms import CheckboxInput


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor',
                  'fecha_publicacion', 'paginas', 'disponible']
        widgets = {'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
                   'disponible': forms.CheckboxInput(),
                   }
