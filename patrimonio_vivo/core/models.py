from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class LugarPatrimonial(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    anio_construccion = models.PositiveIntegerField()
    imagen = models.URLField(blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='lugares'
    )

    def __str__(self):
        return self.nombre
