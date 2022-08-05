from pyexpat import model
from django.db import models
 

# Create your models here.
class Trabajadores(models.Model):
    nombre=models.CharField(max_length=100)
    recibo_honorarios=models.IntegerField()
    pago=models.DecimalField(max_digits=100, decimal_places=2)