from django.db import models
from cloudinary.models import CloudinaryField

class Recuerdo(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    fecha_recuerdo = models.DateField(verbose_name="¿Cuándo pasó?")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_recuerdo']

    def __str__(self):
        return f"{self.fecha_recuerdo} - {self.titulo}"


class MultimediaRecuerdo(models.Model):
    TIPO_CHOICES = [
        ('imagen', 'Imagen'),
        ('video', 'Vídeo'),
    ]
    
    recuerdo = models.ForeignKey(Recuerdo, on_delete=models.CASCADE, related_name='multimedias')
    
    archivo = CloudinaryField('archivo', resource_type='auto')
    
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='imagen', verbose_name="Tipo de archivo")
    pie_de_foto = models.TextField(blank=True, null=True, verbose_name="Pie de foto / vídeo")

    def __str__(self):
        return f"{self.tipo.capitalize()} para: {self.recuerdo.titulo}"