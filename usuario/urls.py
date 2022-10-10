from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import RegistroUsuario,ListadoUsuario
from . import views

urlpatterns = [

    path('registrar_usuario/', RegistroUsuario.as_view(), name="registro_usuario"),
    #path('listar_usuario/', ListadoUsuario.as_view(), name="listar_usuario"),
    path('listar_proveedores/', views.proveedor, name='list_proveedores'),
]