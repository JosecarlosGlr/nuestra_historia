from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('album/<str:nombre_album>/', views.ver_album, name='album'),
    path('borrar-foto/<int:foto_id>/', views.borrar_foto, name='borrar_foto'),
]