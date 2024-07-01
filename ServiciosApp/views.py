from django.shortcuts import render
from ServiciosApp.models import Servicio
# Create your views here.

def servicios(request):
    
    #Con esta instruccion le decimos a Django que en esta variable importe todos los objetos que tengamos creados de ese modelo
    servicios = Servicio.objects.all();
    return render(request, "servicios/servicios.html",{"servicios":servicios})