import requests
from django.shortcuts import render


def index(request):
    api_token = 'bdb3de5d453dc85449f92e059b6fe90b'
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + api_token

    city = 'Minsk'
    res = requests.get(weather_url.format(city))
    print(res.text)

    return render(request, 'weather/home.html')
