from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombres = models.CharField(max_length = 100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length = 100)
    tipoBalon = models.CharField(max_length = 10)