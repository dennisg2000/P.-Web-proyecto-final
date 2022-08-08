from rest_framework import viewsets
from .serializers import BalonSerializer

from .models import Balon
# Create your views here.

class BalonViewSet(viewsets.ModelViewSet):
    queryset = Balon.objects.all()
    serializer_class = BalonSerializer
