from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'animes/home.html')


def form(request):
    return render(request, 'animes/form.html')


def save(request):
    return render(request, 'animes/save.html')


def list(request):
    return render(request, 'animes/list.html')
