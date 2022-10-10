from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum, F, FloatField

from tienda.models import Articulo
from usuario.models import Usuario



class Pedido(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fecha_pedido

    @property
    def total(self):
        return self.detallepedido_set.agregate(
            total = Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering=['id']


class Detalle_Pedido(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} unidades de {self.articulo.nombre}"

    class Meta:
        verbose_name='Detalle Pedido'
        verbose_name_plural='Detalle Pedidos'
        ordering=['id']
