from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('album/<str:nombre_album>/', views.ver_album, name='album'),
]