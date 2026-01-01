from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    """
    Docstring for ProductoViewSet
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
