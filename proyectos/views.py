from django.shortcuts import render

# TODO 1: Para consultar la base de datos, esta vista necesita el modelo.
#         Impórtalo desde el archivo de modelos de esta misma app.


def lista_proyectos(request):
    # TODO 2: Reemplaza la lista vacía por una consulta del ORM que traiga
    #         TODOS los proyectos, del más reciente al más antiguo.
    #         Pista: el ORM se usa a través del "manager" del modelo, y para
    #         invertir un orden hay un símbolo que va antes del nombre del campo.
    proyectos = []

    # TODO 3: Reemplaza el 0 por el número real de proyectos guardados.
    #         Pista: no lo calcules en Python; pídeselo a la base de datos.
    total_proyectos = 0

    contexto = {
        "proyectos": proyectos,
        "total_proyectos": total_proyectos,
    }
    return render(request, "proyectos/lista.html", contexto)
