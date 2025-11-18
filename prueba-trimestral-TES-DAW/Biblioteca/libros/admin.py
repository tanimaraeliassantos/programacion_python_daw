from django.contrib import admin
from .models import Libro


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'creado',
                    'fecha_publicacion', 'disponible', 'paginas', 'creado')

    search_fields = ('titulo', 'autor')

    list_filter = ('disponible', 'fecha_publicacion', 'autor')

    list_editable = ('disponible',)
