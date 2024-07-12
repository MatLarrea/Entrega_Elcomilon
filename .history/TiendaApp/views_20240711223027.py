from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria_producto
from .forms import CategoriaProductoForm, ProductoForm
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
                return redirect('agregar_categoria')  # Redirige a la misma página de agregar categoría
            except IntegrityError:
                messages.error(request, f'La categoría "{nombre_categoria}" ya existe.')
    else:
        form = CategoriaProductoForm()

    categorias = Categoria_producto.objects.all()  # Obtener todas las categorías desde la base de datos

    return render(request, 'tienda/agregar_categoria.html', {'form': form, 'categorias': categorias})

def borrar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria_producto, pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, f'Categoría "{categoria.nombre}" eliminada correctamente.')
        return redirect('agregar_categoria')  # Redirige de nuevo a la misma página de agregar categoría
    return redirect('agregar_categoria')  # En caso de que no sea POST, redirige a la misma página de agregar categoría

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirige a alguna vista o URL después de guardar el producto
            return redirect('nombre_de_tu_vista_o_url')
    else:
        form = ProductoForm()
    
    return render(request, 'tienda/agregar_producto.html', {'form': form})

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        # Redirige a alguna vista o URL después de borrar el producto
        return redirect('nombre_de_tu_vista_o_url')
    
    return render(request, 'tienda/borrar_producto.html', {'producto': producto})