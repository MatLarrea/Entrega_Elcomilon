from django import forms
from .models import Categoria_producto

class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = Categoria_producto
        fields = ['nombre']