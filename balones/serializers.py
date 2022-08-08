from rest_framework import serializers
from .models import Balon

class BalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balon 
        fields = ('id','Lleno','marcaDeEmpresa','Tipo')

