from django import forms
from .models import Conform

class ConformCreateForm(forms.ModelForm):
    class Meta:
        model = Conform
        fields = ['name', 'username']
        labels = {
            'name': 'Ваш никнейм',  # Изменение метки для поля name
            'username': 'Ваш дискорд',  # Изменение метки для поля username
        }
