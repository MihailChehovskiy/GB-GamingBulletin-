from django.shortcuts import render, redirect
from .models import publications
from .forms import publicationsform


def index(request):
    public = publications.objects.order_by('-id')[:10]
    return render(request, 'news/index.html',
                  {'title': 'Главная страницы',
                   'public': public})


def about(request):
    return render(request, 'news/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = publicationsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Поля заполнены некоректно'

    form = publicationsform()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', context)
