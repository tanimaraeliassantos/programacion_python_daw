from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm


def lista_productos(request):
    productos = Producto.objects.filter(
        disponible=True).select_related('categoria')
    return render(request, 'productos/lista_productos.html', {'productos': productos, 'titulo': 'Catálogo de productos'})


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})
