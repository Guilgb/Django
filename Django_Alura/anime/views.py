from django.shortcuts import redirect, render

# Create your views here.


def home(request):
    return render(request, 'animes/home.html')


def form(request):
    if request.method == 'POST':
        print('form preechido com sucesso')
        return redirect('list')
    else:
        return render(request, 'animes/form.html')


def save(request):
    return render(request, 'animes/save.html')


def list(request):
    return render(request, 'animes/list.html')
