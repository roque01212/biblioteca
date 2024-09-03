from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """ Managers para el modelo autor"""

    def listar_autores(self):

        return self.all()
    
    def buscar_autor(self, kword):
        resultado = self.filter(nombre__icontains = kword)
        return resultado
    

    def buscar_autor2(self, kword):
        """Buscar por nombre y apellido"""
        resultado = self.filter(
            Q(nombre__icontains = kword) | Q(apellido__icontains = kword)
            )
        return resultado
    

    def buscar_autor3(self, kword):
        """Excuir edad"""
        resultado = self.filter(
            nombre__icontains = kword
            ).exclude(
                 Q(edad = 80) | Q(edad = 50) # operador O
                 )
        # solo busca las conisidencias de edad
            # .filter(
            #      Q(edad = 80) | Q(edad = 50)
            #      ) 
        return resultado
    
    def buscar_autor4(self, kword):
        """Mayor o igual"""
        resultado = self.filter(
            edad__gt = 40, # mayor
            edad__lt = 65 # menor
            # operador Y
            ).order_by('apellido', 'nombre')
        return resultado