from rest_framework import serializers
from ..models import weatherInfo


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = weatherInfo
        fields = '__all__'