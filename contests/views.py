from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ConformCreateForm
from .models import  Conform

def con(request):
    if request.method == 'POST':
        form = ConformCreateForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['name']
            con = Conform.objects.create(name=input_text)
            con.save()
            messages.success(request, 'Данные успешно отправлены!')
            return redirect('con')  # Перенаправление для предотвращения повторной отправки формы
        else:
            messages.error(request, 'Произошла ошибка при отправке данных.')
    else:
        form = ConformCreateForm()

    return render(request, "index.html", {'name': form})
