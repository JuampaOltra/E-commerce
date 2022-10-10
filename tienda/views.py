from django.db.models import Sum, Q
from ckeditor.widgets import CKEditorWidget
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, TemplateView
from carro.carro import Carro
from .models import Articulo, Categoria, Opinion, Proveedor

from .forms import ArticuloForm

# Create your views here.


# vista de pantalla de inicio
# vista de listado de articulos con barra de busqueda para buscar articulo en la pagina
def listado_articulos(request):
    carro = Carro(request)
    buscar = request.GET.get('buscar')
    articulos = Articulo.objects.filter(publicado=True)

    if buscar:
        articulos = Articulo.objects.filter(
            Q(nombre__icontains=buscar) |
            Q(descripcion__icontains=buscar)
        ).distinct()
        print(articulo)
    return render(request, 'articulos/list_articulos.html', {
        'articulos':articulos,
        'carro':inicio(request),
        'titulo':'E-commerce'
    })



def inicio(request):
    carro = Carro(request)
    return carro


class CrearArticulo(CreateView):
    model = Articulo
    template_name = 'articulos/crear_articulo.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('list_articulos')

    def form_valid(self, form):
        articulo = form.save(commit=False)
        articulo.user = self.request.user
        articulo.save()
        return redirect('list_articulos')




# formulario para editar arituculos
class EditarArticulo(UpdateView):
    model = Articulo
    template_name = 'articulos/crear_articulo.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('list_articulos')

    def get_context_data(self, **kwargs):
        context = super(EditarArticulo, self).get_context_data(**kwargs)
        context['titulo_editar']='EDITAR TÍTULO'
        return context


def proveedor(request, proveedor_id):

    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    articulos = Articulo.objects.filter(proveedor=proveedor)

    return render(request, 'proveedores/proveedores.html',{
    'proveedor': proveedor,
    'articulos':articulos
    })




# pagina con articulos filtrados por categoria
def categoria(request, categoria_id):

    categoria = get_object_or_404(Categoria, id=categoria_id)
    articulos = Articulo.objects.filter(categorias=categoria)

    return render(request, 'categorias/categoria.html',{
        'categoria': categoria,
        'articulos':articulos

    })

# pagina detalle de cada articulo con las opiniones incluidas
def articulo(request, articulo_id):

    articulo = Articulo.objects.get(id= articulo_id)
    opiniones = Opinion.objects.filter(articulo_id=articulo_id)

    return render(request, 'articulos/articulos.html',{
        'articulo':articulo,
        'opiniones':opiniones,


        })

# vista que crea la opiniones
def opinion(request, articulo_id):

    value = request.POST['puntos']
    comment = request.POST['txtopinion']
    user=request.user


    new_opinion = Opinion.objects.create(valor=value, comentario=comment, user_id= user.id, articulo_id=articulo_id)
    opiniones = Opinion.objects.filter(articulo_id=articulo_id)
    articulo = Articulo.objects.get(id=articulo_id)

    return render(request, 'articulos/opinion.html',{
        'opiniones': opiniones,
        'articulo':articulo
    })



