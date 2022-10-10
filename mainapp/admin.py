from django.contrib import admin

# Register your models here.


# cambiamos el nombre del panel de administracion para que sea más amigable


title = "E-commerce"
subtitle = "Panel de Gestión"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle