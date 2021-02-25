import requests
from django.shortcuts import render

from .models import City
from .forms import CityForm


def index(request):
    api_token = 'bdb3de5d453dc85449f92e059b6fe90b'
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_token

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    cities = City.objects.all()
    info = []
    for city in cities:
        res = requests.get(weather_url.format(city.title)).json()
        city_info = {
            'title': city.title,
            'temperature': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
        info.append(city_info)
    context = {'info': info[:3], 'form': form}
    return render(request, 'weather/home.html', context)
