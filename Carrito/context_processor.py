from django.contrib import messages

def importe_total_carro(request):
    
    total = 0
    
    if request.user.is_authenticated:   
        for key, value in request.session["carrito"].items():
            total = total + float(value["precio"])
    else:
        total = "Error"
    return {"importe_total_carro":total}