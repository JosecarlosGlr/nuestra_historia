#!/usr/bin/env bash
# Salir si hay algún error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Empaquetar CSS, JS y Música
python manage.py collectstatic --no-input

# Preparar la base de datos
python manage.py migrate