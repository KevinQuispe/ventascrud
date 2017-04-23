from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=80)
    precio=models.DecimalField(max_digits=5, decimal_places=2)
    stock=models.IntegerField()
   



       