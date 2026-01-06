from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductoForm
from .models import Producto


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos, 'titulo': 'Catálogo de productos'})


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})


def crear_producto(request):
    form = ProductoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        p = form.save()
        return redirect('detalle_producto', producto_id=p.id)
    return render(request, 'productos/crear_producto.html', {'form': form})


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    form = ProductoForm(request.POST or None, instance=producto)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('detalle_producto', producto_id=producto.id)
    return render(request, 'productos/editar_producto.html', {'form': form, 'producto': producto})


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})
