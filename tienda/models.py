from django.core.mail import send_mail
from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django.conf import settings
from usuario.models import Usuario


class Categoria(models.Model):
    nombre = models.CharField(
        'Categoria',
        max_length=50,
    )
    descripcion = RichTextField(
        'Descripción'
    )
    fecha_creacion = models.DateTimeField(
        'Creado'
,        auto_now_add=True
    )
    descuento = models.IntegerField(
        'Decuento',
        default=0,
        blank=True
    )

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(
        'Razon Social',
        max_length=100
    )
    email = models.EmailField(
        blank=False,
        null=False,
        default='1@1.com'
    )
    telefono = models.CharField(
        'telefonos',
        max_length=40,
        blank=True,
    )
    web = models.URLField(
        'sitio web',
        blank=True,
    )
    cif = models.CharField(
        'CIF/NIF',
        max_length=9,
        blank=True,
        null=True,
        unique=True,
    )

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre


"""
    permissions = [('can_add_articulo', 'Puede añadir articulo'), ('can_view_articulo', 'Puede ver articulo'),
                   ('can_add_categoria', 'Puede añadir categoria'), ('can_view_categoria', 'Puede ver categoria')]
"""


class Articulo(models.Model):
    codigo = models.CharField(
        max_length=13,
        unique=True
    )
    nombre = models.CharField(
        'Nombre',
        max_length=40
    )

    proveedor = models.ForeignKey(
        Proveedor,
        default=None,
        on_delete=models.CASCADE
    )

    categorias = models.ManyToManyField(
        Categoria,
        'Categorías',
        default=None,
    )

    user = models.ForeignKey(
        Usuario,
        default=None,
        editable=False,
        on_delete=models.CASCADE)  # editable=False para que el usuario sea el que hace le post y nadie pueda poner un usario que no sea el mismo

    descripcion = RichTextField(
        'Descripcion del producto',
        blank=True,
    )

    caracteristicas = RichTextField(
        'Características'
    )

    image = models.ImageField(
        'Imagen',
        default=None,
        null=True,
        upload_to='fotos_articulos'
    )

    image1 = models.ImageField(
        'Imagen1',
        default=None,
        null=True,
        upload_to='fotos_articulos'
    )

    image2 = models.ImageField(
        'Imagen2',
        default=None,
        null=True,
        upload_to='fotos_articulos'
    )

    image3 = models.ImageField(
        'Imagen2',
        default=None,
        null=True,
        upload_to='fotos_articulos'
    )

    stock = models.PositiveIntegerField(
        'Cantidad en almacen',
        default=0
    )

    stock_minimo = models.PositiveIntegerField(
        'Stock mínimo',
        default=0,

    )

    publicado = models.BooleanField(
        'Publicado/No publicado',
        default=True
    )

    precio = models.DecimalField(
        'Precio',
        max_digits=7,
        decimal_places=2
    )
    num_ventas = models.PositiveIntegerField(
        'Número de ventas',
        default=0
    )

    fecha_de_alta = models.DateTimeField(
        'Fecha de alta',
        auto_now_add=True,
        null=True
    )
    fecha_de_actualizacion = models.DateField(
        'Fecha de actualización',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    def __str__(self):
        return self.nombre

    def disponibilidad(self):
        if self.stock < 1:
            return format_html('<h4 style="color:red;">No disponible</h4>')
        else:
            return format_html('<h4 style="color:green;">En stock</h4>')

    def poco_stock(self):
        if self.stock <= self.stock_minimo:
            stock = self.stock_minimo
            mensaje = f'El stock su artículo {self.nombre} esta en el stock mínimo'
            email_from = settings.EMAIL_HOST_USER
            recipiente = [self.proveedor.email]
            send_mail(stock, mensaje, email_from, recipiente)

            return format_html('<h4 style="color:orange;">Últimas unidades</h4>')
        else:
            return format_html('')

    def total(self):
        total = self.precio * self.num_ventas
        return total


class Opinion(models.Model):
    valor = models.PositiveIntegerField(
        'Valor',
        default=None,
        null=True,
        blank=True)
    comentario = models.TextField(
        'Opinion',
        default=None,
    )

    user = models.ForeignKey(
        Usuario,
        default=None,
        null=True,
        editable=False,
        verbose_name='Opinion Usuario',
        on_delete=models.CASCADE
    )

    articulo = models.ForeignKey(
        Articulo,
        default=None,
        null=False,
        verbose_name='Articulo',
        on_delete=models.CASCADE

    )

    def __str__(self):
        return '{} de {}'.format(self.valor, self.user)

    def estrellas(self):
        if self.valor:
            estrellas = self.valor * '★'
            return estrellas


