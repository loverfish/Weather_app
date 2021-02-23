import requests
from django.shortcuts import render


def index(request):
    api_token = 'bdb3de5d453dc85449f92e059b6fe90b'
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_token

    city = 'Minsk'
    res = requests.get(weather_url.format(city)).json()
    # print()
    # print(res)
    # print()
    # print(res['main']['temp'])
    context = {
        'city': city,
        'temperature': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
    }

    return render(request, 'weather/home.html', context)
