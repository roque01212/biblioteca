from django.db import models
from .managers import AutorManager


# Create your models here.
class Autor(models.Model):
    """Model definition for Autor."""
    nombre = models.CharField('Nombre autor:', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=50)
    edad = models.PositiveIntegerField()
    objects = AutorManager()

    class Meta:
        """Meta definition for Autor."""

        verbose_name = 'Autor'
        verbose_name_plural = 'Autors'

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellido} {self.edad}" 


