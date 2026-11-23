from django.shortcuts import render

# TODO 1: Importa el modelo Proyecto desde models.py
#   from .models import Proyecto


def lista_proyectos(request):
    # TODO 2: Reemplaza la lista vacía por una consulta del ORM que traiga
    #   todos los proyectos ordenados del más reciente al más antiguo:
    #   Proyecto.objects.all().order_by('-fecha_creacion')
    proyectos = []

    # TODO 3: Reemplaza el 0 por una consulta del ORM que cuente los proyectos:
    #   Proyecto.objects.count()
    total_proyectos = 0

    contexto = {
        "proyectos": proyectos,
        "total_proyectos": total_proyectos,
    }
    return render(request, "proyectos/lista.html", contexto)
