from . import views
from django.urls import path

urlpatterns = [
    path('animes/home/', views.home, name='home'),
    path('animes/form/', views.form, name='form'),
    path('animes/save/', views.save, name='save'),
    path('animes/list/', views.list, name='list'),
]
