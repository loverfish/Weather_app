from django import forms

from .models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['title']

        widgets = {'title': forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Введите город'
        })}
