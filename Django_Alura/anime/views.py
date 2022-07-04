from django.shortcuts import redirect, render
from requests import request
from .models import Animes

# Create your views here.


def home(request):
    return render(request, 'animes/home.html')


def form(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        produtora = request.POST['produtora']
        dataLancamento = request.POST['dataLancamento']
        anime = Animes.objects.create(nome=nome, produtora=produtora,
                                      dataLancamento=dataLancamento)
        anime.save()
        return redirect('list')
    else:
        return render(request, 'animes/form.html')


def save(request):
    return render(request, 'animes/save.html')


def list(request):
    animes = Animes.objects.all()
    return render(request, 'animes/list.html', {'animes': animes})


def delete(request, id):
    animes = Animes.objects.get(id=id)
    if request.method == 'POST':
        animes.delete()
        return redirect('animes/list.html')

    return render(request, 'animes/delete.html', {'animes': animes})
