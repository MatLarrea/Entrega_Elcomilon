from django.shortcuts import render
from .models import Producto
from .forms import CategoriaProductoForm
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos":productos})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaProductoForm(request.POST)
        if form.is_valid():
            nombre_categoria = form.cleaned_data['nombre']
            try:
                form.save()
                messages.success(request, f'Categoría "{nombre_categoria}" agregada correctamente.')
                return render(request, 'tienda/agregar_categoria.html', {'form': CategoriaProductoForm()})
            except IntegrityError:
                messages.error(request, f'La categoría "{nombre_categoria}" ya existe.')
    else:
        form = CategoriaProductoForm()
    return render(request, 'tienda/agregar_categoria.html', {'form': form})