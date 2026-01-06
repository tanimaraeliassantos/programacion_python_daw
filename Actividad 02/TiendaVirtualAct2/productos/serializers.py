from rest_framework import serializers
from .models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    """
    Serializador del modelo Producto.
    Convierte objetos Producto en JSON y viceversa.
    """
    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'precio',
            'cantidad',
        ]
