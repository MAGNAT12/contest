from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ConformCreateForm
from .models import  Conform

def con(request):
    if request.method == 'POST':
        form = ConformCreateForm(request.POST)
        if form.is_valid():
            input_name = form.cleaned_data['name']
            input_username = form.cleaned_data['username']
            con = Conform.objects.create(name=input_name, username=input_username)
            con.save()
            messages.success(request, 'Данные успешно отправлены!')
            return redirect('con')  # Перенаправление для предотвращения повторной отправки формы
        else:
            messages.error(request, 'Произошла ошибка при отправке данных.')
    else:
        form = ConformCreateForm()

    return render(request, "index.html", {'name': form})
