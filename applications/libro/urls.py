from django.urls import path
from . import views

app_name = 'libros_app'

urlpatterns = [
    path(
        'libros/', 
        views.LibrosListView.as_view(),
        name='Libros'
        ),
    path(
        'libros2/', 
        views.LibrosListView2.as_view(),
        name='Libros2'
        ),

    path(
        'categoria/', 
        views.LibrosListView2.as_view(),
        name='Categoria'
        ),

    path(
        'libro-detalle/<pk>/', 
        views.LibroDetailView.as_view(),
        name='Libro_detalle'
        ),
]