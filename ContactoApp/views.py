from django.shortcuts import render, redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    formulario = formularioContacto()

    if request.method== "POST":
        #Cargamos la información que usuario mando para poder rescatar su valor
        formulario = formularioContacto(data=request.POST)
        #Preguntamos si se ingresaron todos los datos que corresponden 
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
               
            #Mandamos un email
            email = EmailMessage("Mensaje de Formulario Contacto",
                                "El usuario {}, dirección {}, realizo la siguiente consulta:\n\n {}".format(nombre,email,contenido),"",["mlarreaenvios@outlook.com"], reply_to=[email])
            try :
                email.send()
                return redirect("/contacto/?Datos enviados")
            except Exception as v:
                print({"Error: ":v})
                return redirect("/contacto/?Datos no enviados")
        

    return render(request, "contacto/contacto.html", {"miFormulario": formulario})
