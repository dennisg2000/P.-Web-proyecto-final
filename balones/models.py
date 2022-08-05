from django.db import models

# Create your models here.
class Balon(models.Model):

    Lleno = models.BooleanField(default = True)
    marcaDeEmpresa = models.CharField(max_length = 100)
    Tipo = models.CharField(max_length = 100)

