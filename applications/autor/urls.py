from django.urls import path
from . import views

app_name = 'autores_app'

urlpatterns = [
    path(
        'autores/', 
        views.ListAutores.as_view(), 
        name='Autores'
    ),
]