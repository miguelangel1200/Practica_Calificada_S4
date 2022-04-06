from contextlib import nullcontext
from django.db import models

# Create your models here.

class Region(models.Model):
    nombre_region = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

class Candidato(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre_cand = models.CharField(max_length=250)
    apellido_cand = models.CharField(max_length=250)
    edad = models.IntegerField(default=22)
    ocupacion = models.CharField(max_length=200)

