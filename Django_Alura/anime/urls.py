from django.urls import path

from . import views

app_name = "anime"

urlpatterns = [
    path("", views.AnimeList.as_view(), name="Lista"),
    path("<slug:slug>/", views.AnimeDetail.as_view(), name="detalhes")
]
