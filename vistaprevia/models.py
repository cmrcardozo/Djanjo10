from django.db import models

# Create your models here.

class Producto(models.Model):
	producto = models.CharField(max_length=200)
	fecha_publicacion = models.DateTimeField('Fecha de publicacion')
