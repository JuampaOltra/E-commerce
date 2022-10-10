from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.procesar_pedido, name="pedidos"),

]




