from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Libro, Categoria

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from applications.autor.models import Autor
# Create your views here.



class LibrosListView(ListView):
    context_object_name = 'lista_libros'
    template_name = "libros/lista.html"


    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        #Fecha 1
        fecha1 = self.request.GET.get('fecha1', '')
        # fecha 2
        fecha2 = self.request.GET.get('fecha2', '')
        if fecha1 and fecha2:
            return Libro.objects.listar_libros2(palabra_clave, fecha1, fecha2)

        else:
            return Libro.objects.listar_libros(palabra_clave)
        

  
class LibrosListView2(ListView):
    context_object_name = 'lista_libros'
    template_name = "libros/lista2.html"


    def get_queryset(self):
        
        return Libro.objects.listar_libros_categorias("5")
        

  
class LibrosListView2(ListView):
    context_object_name = 'lista_libros'
    template_name = "libros/categoria.html"


    def get_queryset(self):
        
        return Categoria.objects.listar_categorias_autor("2")
        

      


class LibroDetailView(DetailView):
    model = Libro
    template_name = "libros/detalle.html"

    
    def get_context_data(self, **kwargs):
        context = super(LibroDetailView, self).get_context_data(**kwargs)
        context['autores']=Autor.objects.all()
        return context
    

    def post(self, request, *args, **kwargs):
        libro = self.get_object()  # Recupera el objeto de acuerdo al `pk` en la URL
        autor_id = request.POST.get('autor')
        
        if autor_id:
            autor = get_object_or_404(Autor, id=autor_id)  # Verifica que el autor existe
            libro.autor.remove(autor)  # Agrega el autor al libro
        else:
            # Maneja el caso donde el autor no se envía correctamente
            # Puedes agregar un mensaje de error o manejarlo de alguna otra manera
            pass
        
        # Redirige al mismo detalle del libro después de agregar el autor
        return HttpResponseRedirect(reverse_lazy('libros_app:Libro_detalle', args=[libro.id]))