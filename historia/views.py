from django.shortcuts import render

def pantalla_bienvenida(request):
    return render(request, 'historia/bienvenida.html')