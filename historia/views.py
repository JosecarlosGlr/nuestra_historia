from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from .models import Recuerdo, MultimediaRecuerdo


def bienvenida(request):
    if request.method == 'POST':
        palabra_secreta = request.POST.get('password', '')
        
        if palabra_secreta.lower() == '506':
            return render(request, 'historia/bienvenida.html')
        else:
            return render(request, 'historia/login.html', {'error': 'Esa no es la palabra correcta...'})
    
    return render(request, 'historia/login.html')

def añadir_recuerdo(request):
    if request.method == 'POST':
        # 1. Recogemos los datos generales del recuerdo
        titulo = request.POST.get('titulo')
        fecha = request.POST.get('fecha')
        
        # Guardamos el recuerdo principal en Neon
        recuerdo = Recuerdo.objects.create(titulo=titulo, fecha_recuerdo=fecha)
        
        # 2. Recogemos las listas de archivos y sus pies de foto
        archivos = request.FILES.getlist('archivos')
        pies_de_foto = request.POST.getlist('pies_de_foto')
        
        # Recorremos cada archivo subido
        for i, archivo in enumerate(archivos):
            # Detectamos si es vídeo o imagen por su extensión
            extension = archivo.name.split('.')[-1].lower()
            tipo = 'video' if extension in ['mp4', 'mov', 'avi', 'mkv'] else 'imagen'
            
            # Cogemos el pie de foto que le corresponde a esta posición
            pie = pies_de_foto[i] if i < len(pies_de_foto) else ""
            
            # Guardamos cada foto/vídeo conectado a este recuerdo
            MultimediaRecuerdo.objects.create(
                recuerdo=recuerdo,
                archivo=archivo,
                tipo=tipo,
                pie_de_foto=pie
            )
            
        return redirect('bienvenida') # Al terminar, volvemos a la pantalla principal
        
    return render(request, 'historia/añadir_recuerdo.html')

def ver_album(request, nombre_album):
    # 1. Convertimos el nombre clave ("primer_viaje") en un título bonito ("Primer viaje")
    titulo_bonito = nombre_album.replace('_', ' ').capitalize()
    
    # 2. Buscamos el álbum en la base de datos. Si no existe aún, lo crea al instante.
    recuerdo, creado = Recuerdo.objects.get_or_create(
        titulo=titulo_bonito,
        defaults={'fecha_recuerdo': date.today()} 
    )

    # 3. Si rellenáis el formulario para añadir más fotos a este álbum
    if request.method == 'POST':
        archivos = request.FILES.getlist('archivos')
        pies_de_foto = request.POST.getlist('pies_de_foto')
        
        for i, archivo in enumerate(archivos):
            extension = archivo.name.split('.')[-1].lower()
            tipo = 'video' if extension in ['mp4', 'mov', 'avi', 'mkv'] else 'imagen'
            pie = pies_de_foto[i] if i < len(pies_de_foto) else ""
            
            MultimediaRecuerdo.objects.create(
                recuerdo=recuerdo,
                archivo=archivo,
                tipo=tipo,
                pie_de_foto=pie
            )
        # Al terminar de subir, recargamos la misma página para ver las fotos nuevas
        return redirect('album', nombre_album=nombre_album)

    # 4. Cogemos todas las fotos que ya existen en este álbum para mostrarlas
    galeria = recuerdo.multimedias.all()
    
    return render(request, 'historia/album.html', {
        'recuerdo': recuerdo,
        'galeria': galeria
    })

def borrar_foto(request, foto_id):
    # Buscamos el recuerdo exacto en la base de datos
    foto = get_object_or_404(MultimediaRecuerdo, id=foto_id)
    
    # Lo eliminamos (esto lo borrará de Neon y de Cloudinary)
    foto.delete()
    
    # Este truco devuelve a la usuaria a la misma página del álbum donde estaba
    return redirect(request.META.get('HTTP_REFERER', 'bienvenida'))