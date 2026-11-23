from django.db import models

# TODO 1: Crea una clase llamada Proyecto que herede de models.Model.
#
# TODO 2: Agrega los siguientes campos al modelo:
#   - titulo           -> models.CharField(max_length=200)
#   - tecnologia       -> models.CharField(max_length=100)
#   - horas_desarrollo -> models.IntegerField()
#   - fecha_creacion   -> models.DateTimeField(auto_now_add=True)
#
# TODO 3: Define el método __str__(self) para que devuelva el título del proyecto.
#
# TODO 4: Cuando termines, genera y aplica las migraciones:
#   python manage.py makemigrations
#   python manage.py migrate
