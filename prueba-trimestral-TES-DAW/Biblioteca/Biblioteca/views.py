from django.shortcuts import render
from django.http import HttpResponse


def productos_list(request):
    return HttpResponse("Lista de productos")
