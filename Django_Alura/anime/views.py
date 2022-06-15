from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Anime

# Create your views here.

class AnimeList(ListView):
    model = Anime

class AnimeDetail(DetailView):
    model = Anime