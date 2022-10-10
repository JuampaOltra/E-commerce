from .models import Categoria, Articulo

def get_categories(request):

    categorias_in_use = Articulo.objects.filter(publicado=True).values_list('categorias', flat=True) # flat es en formato plano
    categorias = Categoria.objects.filter(id__in=categorias_in_use).values_list('id', 'nombre')

    return {
        'categorias':categorias,
        'ids': categorias_in_use,
        'titulo':'E-commerce'
    }