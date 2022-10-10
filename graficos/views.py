
from django.views.generic import TemplateView

from tienda.models import Articulo


class Graficos(TemplateView):
    template_name = 'graficos.html'


    def get_datos_grafico_articulos_mas_precio(self):
        series=[]

        articulos = Articulo.objects.all().order_by('-precio')[:5]
        for a in articulos:
            series.append( {
            'name':a.nombre,
            'data':[int(a.precio), ]
        })

        return series

    def get_nombre_articulos_mas_precio(self):
        categorias = []
        articulos = Articulo.objects.all().order_by('precio')[:5]
        for a in articulos:
            categorias.append(a.nombre)


        return categorias

    def get_datos_grafico_articulos_mas_vendidos(self):
        data = []
        articulos = Articulo.objects.all().order_by('-num_ventas')[:5]
        for a in articulos:
            data.append(
                [a.nombre, a.num_ventas])
        return data

    def get_nombre_articulos_mas_vendidos(self):
        categorias = []
        articulos = Articulo.objects.all().order_by('-num_ventas')[:5]
        for a in articulos:
            categorias.append(a.nombre)
        return categorias

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['series_mas_precio'] = self.get_datos_grafico_articulos_mas_precio()
        context['nombres_mas_vendidos'] = self.get_nombre_articulos_mas_vendidos()
        context['series_mas_vendidos'] = self.get_datos_grafico_articulos_mas_vendidos()

        return context



