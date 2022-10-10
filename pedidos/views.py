from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from carro.carro import Carro

from pedidos.models import Pedido, Detalle_Pedido
from tienda.models import Articulo


@login_required(login_url="/login/")
def procesar_pedido(request):

    pedido = Pedido.objects.create(usuario=request.user)
    carro=Carro(request)
    detalles_pedido=list()

    for key, value in carro.carro.items():
        articulo = Articulo.objects.get(id=key)
        detalles_pedido.append(Detalle_Pedido(
            articulo_id=key,
            cantidad=value["cantidad"],
            usuario=request.user,
            pedido=pedido
        ))

        articulo.stock = articulo.stock - value['cantidad']
        articulo.num_ventas = articulo.num_ventas + value['cantidad']
        articulo.save()
    Detalle_Pedido.objects.bulk_create(detalles_pedido)

    enviar_email(
        pedido=pedido,
        detalles_pedido=detalles_pedido,
        nombre_usuario=request.user.username,
        email_usuario=request.user.email
    )

    messages.success(request, "El pedido se ha creado correctamente")

    carro.limpiar_carro()

    return redirect('inicio')

def enviar_email(**kwargs):

    asunto="Gracias por realizar su pedido"
    mensaje=render_to_string('pedidos/pedidos.html',{
        'pedido':kwargs.get('pedido'),
        'detalles_pedido':kwargs.get('detalles_pedido'),
        'nombre_usuario':kwargs.get('nombre_usuario')
    })
    mensaje_texto=strip_tags(mensaje)
    from_email="lalataaudiovisual@gmail.com"
    to=kwargs.get('email_usuario')

    send_mail(asunto, mensaje_texto,from_email,[to], html_message=mensaje)


