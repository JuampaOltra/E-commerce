from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Usuario
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    #inlines = [ImagenProductoTabular]
    search_fields = ('cif', 'email')
    list_display = ('username','cif', 'is_staff','is_proveedor')



admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Permission)