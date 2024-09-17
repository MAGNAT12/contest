from django import forms
from .models import Conform

class ConformCreateForm(forms.ModelForm):
    class Meta:
        model = Conform
        fields = ['name']  # Убедитесь, что поле 'name' существует в модели
