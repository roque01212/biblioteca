import datetime
from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):
    """ Managers para el modelo autor"""

    def listar_libros(self, kword):
        """Filtro por fechas"""
        resultado = self.filter(
            titulo__icontains = kword,
            fecha__range = ('2020-01-01', '2024-12-12')
        )
        return resultado
    

    def listar_libros2(self, kword, fecha1, fecha2):
        """Filtro por fechas"""
        date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d').date()
        resultado = self.filter(
            titulo__icontains = kword,
            fecha__range = (date1, date2)
        )
        return resultado
    

    def listar_libros_categorias(self, categoria):
        """FILTRADO LOS LIBROS QUE PERTENECEN A ALGUNA CATEGORIA"""
        return self.filter(
            categoria__id = categoria
            ).order_by('titulo')
    
    def add_autor_libro(self, libro_id, autor):
        """AGREGANDO UN NUEVO AUTOR A UN LIBRO"""
        libro = self.get(id = libro_id) # RECUPERAMOS UN SOLO LIBRO
        libro.autor.remove(autor) # ADD YA TRAE LA RELACION M2M
        # libro.autor.remove(autor) ESTO ELIMINARIA UN AUTOR
        return libro



class CategoriaManager(models.Manager):

    def listar_categorias_autor(self, autor):
        """RECUPERAR CATEGORIAS POR AUTOR"""
        return self.filter(
            categoria_libro__autor__id = autor
        ).distinct()# evitar que se repita
    
