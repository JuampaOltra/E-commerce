# Generated by Django 4.0.6 on 2022-08-22 16:22

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=13, unique=True)),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripcion del producto')),
                ('caracteristicas', models.TextField(verbose_name='Características')),
                ('image', models.ImageField(default='null', upload_to='fotos_articulos', verbose_name='Imagen')),
                ('cantidad', models.PositiveIntegerField(default=0, verbose_name='Cantidad a comprar')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Cantidad en almacen')),
                ('publicado', models.BooleanField(default=True, verbose_name='Publicado/No publicado')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Precio')),
                ('num_ventas', models.PositiveIntegerField(default=0, verbose_name='Número de ventas')),
                ('fecha_de_alta', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de alta')),
                ('fecha_de_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Artículo',
                'verbose_name_plural': 'Artículos',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Categoria')),
                ('descripcion', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('descuento', models.IntegerField(blank=True, default=0, verbose_name='Decuento')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Razon Social')),
                ('email', models.EmailField(default='1@1.com', max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=40, verbose_name='telefonos')),
                ('web', models.URLField(blank=True, verbose_name='sitio web')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Valor')),
                ('comentario', models.TextField(default=None, verbose_name='Opinion')),
                ('articulo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tienda.articulo', verbose_name='Articulo')),
                ('user', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Opinion Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='categorias',
            field=models.ManyToManyField(default=None, related_name='Categorías', to='tienda.categoria'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='proveedor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tienda.proveedor'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='user',
            field=models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]