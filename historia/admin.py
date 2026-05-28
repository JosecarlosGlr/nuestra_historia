from django.contrib import admin
from .models import Recuerdo, MultimediaRecuerdo

# Esto permite meter los archivos multimedia directamente dentro de la pantalla del Recuerdo
class MultimediaInline(admin.TabularInline):
    model = MultimediaRecuerdo
    extra = 1  # Te muestra un hueco vacío por defecto para subir la primera foto
    fields = ['archivo', 'tipo', 'pie_de_foto']

@admin.register(Recuerdo)
class RecuerdoAdmin(admin.ModelAdmin):
    list_display = ['fecha_recuerdo', 'titulo']
    inlines = [MultimediaInline] # Metemos el bloque de fotos dentro del recuerdo