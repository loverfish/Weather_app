import requests

from .models import City
from .forms import CityForm


api_token = 'bdb3de5d453dc85449f92e059b6fe90b'
weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_token


def post_exceptions(request):

    error_dict = {}
    if request.method == 'POST':
        try:
            res = requests.get(weather_url.format(request.POST['title'])).json()
            a, b = res['main']['temp'], res['weather'][0]['icon']
        except KeyError:
            error_dict = {'exception': 'Неверно указан город'}
            print(error_dict['exception'])
        else:
            form = CityForm(request.POST)
            form.save()

    return error_dict


def cities_list():
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
    return info
