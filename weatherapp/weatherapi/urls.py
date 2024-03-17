from django.urls import path
from .views import *

urlpatterns = [
    path('', WeatherDataView.as_view({'get': 'list'}), name="api-weather-info")
]