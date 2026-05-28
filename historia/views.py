from django.shortcuts import render

def bienvenida(request):
    if request.method == 'POST':
        palabra_secreta = request.POST.get('password', '')
        
        if palabra_secreta.lower() == '506':
            return render(request, 'historia/bienvenida.html')
        else:
            return render(request, 'historia/login.html', {'error': 'Esa no es la palabra correcta...'})
    
    return render(request, 'historia/login.html')