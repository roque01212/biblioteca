from django.db import models
from applications.libro.models import Libro
# Create your models here.


class Lector(models.Model):
    """Model definition for Lector."""

    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=50)
    edad = models.PositiveIntegerField()

    class Meta:
        """Meta definition for Lector."""

        verbose_name = 'Lector'
        verbose_name_plural = 'Lectors'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Prestamo(models.Model):
    """Model definition for Prestamo."""
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField('Fecha prestamo', auto_now=False, auto_now_add=False)
    fecha_devuelto = models.DateField('Fecha devolucion', blank=True, null=True)
    devueto = models.BooleanField()


    class Meta:
        """Meta definition for Prestamo."""

        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):
        return self.libro.titulo
