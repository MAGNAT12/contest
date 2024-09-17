from django.shortcuts import render
from .models import Conform
from .forms import ConformCreateForm

def con(request):
    if request.method == 'POST':
        form = ConformCreateForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['name']  # Используем данные из формы
            con = Conform.objects.create(name=input_text)
            con.save()
    else:
        form = ConformCreateForm()

    return render(request, "index.html", {'name': form})
