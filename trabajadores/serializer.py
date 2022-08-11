from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import Trabajadores

class TrabajadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajadores
        fields = ('id','nombre','recibo_honorarios','pago')
