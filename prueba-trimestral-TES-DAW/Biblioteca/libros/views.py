from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm


def libro_lista(request):
    libros = Libro.objects.all()
    return render(request, 'libros/libro_lista.html', {'libros': libros})


def libro_detalle(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/libro_detalle.html', {'libro': libro})


def libro_crear(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)

        if form.is_valid():
            libro = form.save()
            return redirect('libro_detalle', pk=libro.pk)
    else:
        form = LibroForm()

    context = {'form': form, 'titulo': 'Crear Nuevo Libro'}
    return render(request, 'libros/libro_formulario.html', context)


def libro_editar(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)

        if form.is_valid():
            form.save()

            return redirect('libro_detalle', pk=pk)
    else:
        form = LibroForm(instance=libro)
    context = {'form': form, 'titulo': f'Editar Libro: {libro.titulo}'}
    return render(request, 'libros/libro_formulario.html', context)


def eliminar_libro(request, pk):

    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        libro.delete()
        return redirect('libro_lista')

    context = {'libro': libro}
    return render(request, 'libros/eliminar_libro.html', context)
