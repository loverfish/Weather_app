import requests
from django.shortcuts import render

from .models import City
from .forms import CityForm


def index(request):
    api_token = 'bdb3de5d453dc85449f92e059b6fe90b'
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_token

    error_dict = {}
    if request.method == 'POST':
        try:
            res = requests.get(weather_url.format(request.POST['title'])).json()
            a, b = res['main']['temp'], res['weather'][0]['icon']
        except Exception:
            error_dict = {'exception': 'неверный город'}
            print(error_dict['exception'])
        else:
            form = CityForm(request.POST)
            form.save()
    form = CityForm()

    cities = City.objects.all()
    info = []
    for city in cities[:3]:
        res = requests.get(weather_url.format(city.title)).json()
        city_info = {
            'title': city.title,
            'temperature': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
        info.append(city_info)
    context = {'info': info, 'form': form, 'error_dict': error_dict}
    return render(request, 'weather/home.html', context)
