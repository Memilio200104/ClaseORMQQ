from django.db import models

# TODO 1: Crea el modelo Proyecto. Recuerda: en Django, un modelo es una clase
#         que hereda de algo que viene dentro de "models".
#
# TODO 2: Agrega estos cuatro campos. Piensa qué tipo de campo le queda a cada uno:
#   - titulo           -> texto corto (¿qué argumento es obligatorio en este tipo de campo?)
#   - tecnologia       -> texto corto, p. ej. "Django", "React"
#   - horas_desarrollo -> un número entero
#   - fecha_creacion   -> fecha y hora que se llene SOLA al crear el registro
#                         (nadie debería escribirla a mano)
#
# TODO 3: Haz que cada proyecto se muestre con su título (en el admin y en la
#         shell), en lugar de "Proyecto object (1)". ¿Qué método especial de
#         Python controla cómo se ve un objeto como texto?
