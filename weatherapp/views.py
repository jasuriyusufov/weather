import requests
from django.shortcuts import render, redirect
from .models import weatherInfo

# Create your views here.


def main(request):
    weatherInfo.objects.all()

    return render(request, 'weatherapp/index.html')


def weather_data(request):
    api = "47113998a9426d89bff31a0a1116999c"
    city = "Glasgow"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'

    wd = requests.get(url)
    dataJs = wd.json()

    mdl = weatherInfo.objects.all()
    for weather_data in mdl:
        weatherInfo.objects.get(pk=weather_data.id).delete()

    weather = weatherInfo(city=dataJs["name"], temperature=dataJs["main"]["temp"], humidity=dataJs["main"]["humidity"])
    weather.save()

    return redirect('main')
