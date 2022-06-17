from django.contrib import admin
from .models import Animes

# Register your models here.
@admin.register(Animes)
class AdminAnime(admin.ModelAdmin):
    list_display = ('idAnime', 'nomeAnime', 'dataLancamento')