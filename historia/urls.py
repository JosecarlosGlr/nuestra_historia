from django.urls import path
from . import views

urlpatterns = [
    path('', views.pantalla_bienvenida, name='bienvenida'),
]