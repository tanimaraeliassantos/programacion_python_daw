from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    """
    API REST para gestionar productos.

    Permite realizar las operaciones CRUD:
    - Crear
    - Consultar
    - Actualizar
    - Eliminar
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
