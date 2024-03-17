from rest_framework import viewsets
from .serializers import *


class WeatherDataView(viewsets.ModelViewSet):
    serializer_class = WeatherSerializer
    queryset = weatherInfo.objects.all()
