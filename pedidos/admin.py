from django.contrib import admin
from .models import Pedido, Detalle_Pedido

# Register your models here.

admin.site.register(Pedido)
admin.site.register(Detalle_Pedido)