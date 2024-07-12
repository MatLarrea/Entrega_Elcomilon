from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Carrito.carro import Carrito
from .models import LineaPedido, Pedido
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.

#Instrucción para especificar q el usuario debe estar logeado para hacer un pedido
@login_required(login_url="/AutentificacionApp/logear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carrito(request)
    lineas_pedido = list()
    
    #rellenamos nuestra listas con los productos que pidio el usuario
    for key, value in carro.carrito.items():
        lineas_pedido.append(
            LineaPedido(
                producto_id = key,
                cantidad = value["cantidad"],
                user=request.user,
                pedido=pedido
            )
        )
    
    #bulk_create: simula un insert into en la base de datos como lo harias con un cursor
    LineaPedido.objects.bulk_create(lineas_pedido)
    enviar_mail(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        usuario = request.user.username,
        email_usuario = request.user.email
    )
    return redirect("../tienda")

def enviar_mail(**kwargs):
    
    asunto = "Pedido Confirmado"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "usuario": kwargs.get("usuario")
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = "mlarreaenvios@outlook.com"
    to = kwargs.get("email_usuario")
    send_mail(
        asunto,
        mensaje_texto,
        from_email,
        [to],
        html_message = mensaje
    )