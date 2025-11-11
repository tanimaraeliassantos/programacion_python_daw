from django.contrib import admin
from .models import Categoria, Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'disponible', 'categoria')
    list_filter = ('disponible', 'categoria')
    search_fields = ('nombre', 'descripcion')

    list_editable=('precio', 'stock', 'disponible')


admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
