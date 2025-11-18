from django.urls import path
from .import views

urlpatterns = [
    path('', views.libro_lista, name='libro_lista'),
    path('<int:libro_id>/', views.libro_detalle, name='libro_detalle'),
    path('nuevo/', views.libro_crear, name='libro_crear'),
    path('<int:libro_id>/editar/', views.libro_editar, name='libro_editar'),
    path('<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
]
