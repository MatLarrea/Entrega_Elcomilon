from django.shortcuts import render, redirect
from .models import Producto
from .forms import CategoriaProductoForm

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos":productos})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_tu_vista_o_url')
    else:
        form = CategoriaProductoForm()
    return render(request, 'agregar_categoria.html', {'form': form})