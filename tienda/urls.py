from django.urls import path
from . import views
from .views import CrearArticulo, EditarArticulo

urlpatterns = [
    path('articulos/', views.listado_articulos, name="list_articulos"),
    path('listar_proveedores/<int:proveedor_id>', views.proveedor, name='list_proveedores'),
    path('categoria/<int:categoria_id>',views.categoria, name="categoria"),
    path('crear_articulook/', CrearArticulo.as_view(), name='crear_articulo'),
    path('articulo/<int:articulo_id>', views.articulo, name="articulo"),
    path('editar_articulo/<int:pk>', EditarArticulo.as_view(), name='editar_articulo'),
    path('opinion/ <int:articulo_id>', views.opinion, name="opinion"),

]




