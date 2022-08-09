from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .serializer import TrabajadoresSerializer
from .models import Trabajadores

# Create your views here.
class TrabajadoresViewSet(viewsets.ModelViewSet):
    queryset = Trabajadores.objects.all()
    serializer_class = TrabajadoresSerializer 

