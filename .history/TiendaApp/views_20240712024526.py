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
                return redirect('agregar_categoria')
            except IntegrityError:
                messages.error(request, f'La categoría "{nombre_categoria}" ya existe.')
    else:
        form = CategoriaProductoForm()

    categorias = Categoria_producto.objects.all() 

    return render(request, 'tienda/agregar_categoria.html', {'form': form, 'categorias': categorias})

def borrar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria_producto, pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, f'Categoría "{categoria.nombre}" eliminada correctamente.')
        return redirect('agregar_categoria') 
    return redirect('agregar_categoria')  
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agregar_producto')
    else:
        form = ProductoForm()
    
    productos = Producto.objects.all()
    context = {
        'form': form,
        'productos': productos,
    }
    return render(request, 'tienda/agregar_producto.html', context)

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('agregar_producto')
    
    return render(request, 'tienda/agregar_producto.html', {'producto': producto})