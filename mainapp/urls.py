from django.urls import path
from django.contrib.auth.decorators import login_required
#from .views import inicio
import tienda
import usuario
from tienda.views import listado_articulos
from usuario.views import Inicio, Login, logout_user

urlpatterns = [


    path('', tienda.views.listado_articulos, name='inicio'),
    path('inicio', tienda.views.listado_articulos, name='inicio'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', login_required(logout_user), name='logout')
]
