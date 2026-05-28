from django.db import models

class Recuerdo(models.Model):
    # El recuerdo ahora solo guarda los datos generales del día
    titulo = models.CharField(max_length=200, verbose_name="Título")
    fecha_recuerdo = models.DateField(verbose_name="¿Cuándo pasó?")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_recuerdo']

    def __str__(self):
        return f"{self.fecha_recuerdo} - {self.titulo}"


class MultimediaRecuerdo(models.Model):
    # Opciones para saber si lo que subimos es foto o vídeo (útil para el carrusel HTML)
    TIPO_CHOICES = [
        ('imagen', 'Imagen'),
        ('video', 'Vídeo'),
    ]
    
    # Esta línea conecta este archivo con un Recuerdo específico. Si se borra el recuerdo, se borran sus fotos (CASCADE)
    recuerdo = models.ForeignKey(Recuerdo, on_delete=models.CASCADE, related_name='multimedias')
    
    archivo = models.FileField(upload_to='recuerdos/', verbose_name="Foto o Vídeo")
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='imagen', verbose_name="Tipo de archivo")
    pie_de_foto = models.TextField(blank=True, null=True, verbose_name="Pie de foto / vídeo")

    def __str__(self):
        return f"{self.tipo.capitalize()} para: {self.recuerdo.titulo}"