from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('weather/', weather_data, name='weather_data')
]