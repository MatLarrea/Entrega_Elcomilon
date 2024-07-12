from django.shortcuts import render
from .models import Producto
from .forms import CategoriaProductoForm
from django.contrib import messages


# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos":productos})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La categoría se ha agregado correctamente.')
            return render(request, 'tienda/agregar_categoria.html', {'form': CategoriaProductoForm()})
    else:
        form = CategoriaProductoForm()
    return render(request, 'tienda/agregar_categoria.html', {'form': form})