from django.shortcuts import render, redirect
from django.utils.html import format_html
from .carro import Carro
from tienda.models import Articulo

def mostrar_articulos_carro(request):
    carro=Carro(request)
    return render(request, 'articulos/carro.html', {
        'carro':carro
    })

def agregar_articulo_carro(request, articulo_id):
    carro = Carro(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carro.agregar_articulo(articulo=articulo)

    return render(request, 'articulos/articulos.html',{
        'articulo':articulo
    } )


def eliminar_articulo_carro(request, articulo_id):
    carro = Carro(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carro.eliminar_articulo(articulo=articulo)
    return redirect ('list_articulos')

def restar_articulo_carro(request, articulo_id):
    carro = Carro(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carro.restar_articulo(articulo=articulo)
    return redirect ('list_articulos')

def limpiar_carro_articulos(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect ('list_articulos')
