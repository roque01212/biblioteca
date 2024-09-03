from django.db import models
from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager

# Create your models here.
class Categoria(models.Model):
    """Model definition for Categoria."""
    nombre = models.CharField('Nombre', max_length=30)

    objects = CategoriaManager()


    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f"{self.id} {self.nombre}"

class Libro(models.Model):
    """Model definition for Libro."""
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, 
        related_name='categoria_libro'
        )
    autor = models.ManyToManyField(Autor)
    titulo = models.CharField(
        'Titulo', 
        max_length=50)
    fecha = models.DateField('fecha de lanzamiento', 
        auto_now=False, 
        auto_now_add=False
        )
    portada = models.ImageField( 
        upload_to='portada',
        )
    visitas = models.PositiveIntegerField()
    objects = LibroManager()

    class Meta:
        """Meta definition for Libro."""

        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
       return f"{self.titulo}"
    
    
