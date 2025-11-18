from django.urls import path
from .import views

urlpatterns = [
    path('', views.libro_lista, name='libro_lista'),
    path('<int:libro_id>/', views.libro_detalle, name='libro_detalle'),
    path('nuevo/', views.libro_formulario, name='libro_formulario'),
    path('<int:libro_id>/editar/', views.libro_formulario, name='libro_formulario'),
    path('<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
]
