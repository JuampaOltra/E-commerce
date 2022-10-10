from django.contrib import admin
from django.utils.html import strip_tags

from .models import Categoria, Articulo, Opinion, Proveedor
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class ArticuloResource(resources.ModelResource):
    class Meta:
        model = Articulo



class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'id')
    readonly_fields = ('fecha_creacion',)
    resources_class = CategoriaResource

class ArticuloAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    readonly_fields = ('user','fecha_de_alta', 'fecha_de_actualizacion', 'num_ventas')
    search_fields = ('nombre', 'descripcion', 'caracteristicas')
    list_display = ('nombre', 'sinTag', 'proveedor','num_ventas', 'id')
    list_filter = ('proveedor', 'categorias')
    resources_class = ArticuloResource


    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()


    def sinTag(self, obj):
        return strip_tags(obj.descripcion)

    def datos(self, obj):
        return strip_tags(obj.caracteristicas.title())


class OpinionAdmin(admin.ModelAdmin):

    list_display = ('valor', 'articulo', 'user')






# Register your models here.

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Articulo, ArticuloAdmin )
admin.site.register(Opinion, OpinionAdmin)
admin.site.register(Proveedor)