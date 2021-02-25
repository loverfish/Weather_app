from django.shortcuts import render

from .forms import CityForm
from .utilits import post_exceptions, cities_list


def index(request):
    error_dict = post_exceptions(request)
    form = CityForm()
    info = cities_list()
    context = {'info': info, 'form': form, 'error_dict': error_dict}
    return render(request, 'weather/home.html', context)
