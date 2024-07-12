from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, CategoriaProducto
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

def borrar_categoria(request, categoria_id):
    categoria = get_object_or_404(CategoriaProducto, pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, f'Categoría "{categoria.nombre}" eliminada correctamente.')
        return redirect('agregar_categoria')  # Redirige de nuevo a la misma página de agregar categoría
    return render(request, 'tienda/agregar_categoria.html', {'categoria': categoria})