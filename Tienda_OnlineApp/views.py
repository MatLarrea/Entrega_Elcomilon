from django.shortcuts import render, HttpResponse

from Carrito.carro import Carrito

# Create your views here.


def home(request):
    carrito = Carrito(request)
    return render(request, "Tienda_OnlineApp/home.html")





