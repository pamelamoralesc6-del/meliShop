from django.db import models

class Productos(models.Model):
    talla = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    tipo_tela = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    stock = models.CharField(max_length=100)
    imagen_url = models.CharField(max_length=500)

def __str__ (self):
    return f"{self.talla} {self.precio} {self.tipo_tela}"