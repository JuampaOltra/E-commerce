from django.utils.html import format_html

def importe_total_carro(request):
    total = 0
    cantidad = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total + float(value['precio'])
            cantidad = cantidad + value['cantidad']
            value['stock'] = value['stock'] - value['cantidad']
            print(request.session["carro"].items())
    return {'importe_total_carro': total,
            'numero_articulos': cantidad,
            }

