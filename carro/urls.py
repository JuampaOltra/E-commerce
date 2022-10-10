from django.urls import path
from . import views

urlpatterns = [
    path('carro', views.mostrar_articulos_carro, name="listar_carro"),
    path('agregar_articulo_carro/<int:articulo_id>', views.agregar_articulo_carro, name="agregar_articulo_carro"),
    path('eliminar_articulo_carro/<int:articulo_id>', views.eliminar_articulo_carro, name="eliminar_articulo_carro"),
    path('restar_articulo_carro/<int:articulo_id>', views.restar_articulo_carro, name="restar_articulo_carro"),
    path('limpiar_carro', views.limpiar_carro_articulos, name="limpiar_carro")

]