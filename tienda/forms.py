from django import forms
from .models import Proveedor, Articulo
from ckeditor.widgets import CKEditorWidget



class ArticuloForm(forms.ModelForm):

    class Meta:

        model = Articulo

        fields = ['codigo', 'nombre', 'proveedor', 'categorias', 'descripcion', 'caracteristicas', 'image', 'image1',
                  'image2', 'image3', 'stock', 'stock_minimo', 'publicado', 'precio']

        labels = {
            'codigo': 'Número de código',
            'nombre': 'Nombre del articulo',
            'proveedor': 'Proveedor',
            'descripcion': 'Descripcion',
            'caracteristicas': 'Caracteristicas',
            'categorias': 'Categoria',
            'image': 'Imagen',
            'image1': 'Imagen 1',
            'image2': 'Imagen 2',
            'image3': 'Imagen 3',
            'stock': 'Número en almacen',
            'stock_minimo': 'Mínimo de artículos',
            'publicado': 'Publicado',
            'precio': 'Precio',
        }

        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Número de código'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del articulo'
                }
            ),

            'proveedor': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'proveedor'
                }
            ),
            'descripcion': CKEditorWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'descripcion'
                }
            ),
            'caracteristicas': CKEditorWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'caracteristicas'
                }
            ),
            'categorias': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Web del proveedor'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Imagen'
                }
            ),
            'image1': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Imagen'
                }
            ),
            'image2': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Imagen'
                }
            ),
            'image3': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Imagen'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Num en almacen'
                }
            ),
            'stock_minimo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Mínimo de articulos para avisarte'
                }
            ),
            'publicado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Mínimo de articulos para avisarte'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio'
                }
            ),
            'num_ventas': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Num de ventas'
                }
            )

        }
