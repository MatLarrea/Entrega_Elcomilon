from django import forms
from .models import Categoria_producto, Producto

class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = Categoria_producto
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categorias', 'imagen', 'disponibilidad']