from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

class VRegistro(View):
   
    def get(self, request):
        form=UserCreationForm()
        return render(request, "autentificacion/registro.html", {"form": form})
     
    def post(self, request):
        
        form=UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                return render(request, "autentificacion/registro.html", {"form": form})

def logear(request):
    

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            #Autentificacion del usuario
            usuario = authenticate(username = nombre_usuario, password = contrasena)
        
            if usuario is not None:
                login(request, usuario)
                return redirect("home")
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")

    form = AuthenticationForm()
    return render(request, "login/login.html", {"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect("home")