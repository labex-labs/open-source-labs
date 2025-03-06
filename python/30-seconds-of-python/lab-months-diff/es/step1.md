# Comprender los objetos de fecha en Python

Antes de calcular la diferencia en meses entre fechas, necesitamos entender cómo trabajar con objetos de fecha en Python. En este paso, aprenderemos sobre el módulo `datetime` y crearemos algunos objetos de fecha.

Primero, creemos un nuevo archivo de Python en el directorio del proyecto. Abrir el WebIDE y hacer clic en el icono "Nuevo archivo" en el panel del explorador en el lado izquierdo. Nombrar el archivo `month_difference.py` y guardarlo en el directorio `/home/labex/project`.

Ahora, agreguemos el siguiente código para importar los módulos necesarios:

```python
from datetime import date
from math import ceil

# Create example date objects
date1 = date(2023, 1, 15)  # January 15, 2023
date2 = date(2023, 3, 20)  # March 20, 2023

# Print the dates to see their format
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")

# Calculate the difference in days
day_difference = (date2 - date1).days
print(f"Difference in days: {day_difference}")
```

Guardar el archivo y ejecutarlo utilizando la terminal:

```bash
python3 ~/project/month_difference.py
```

Deberías ver una salida similar a esta:

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
```

La clase `date` del módulo `datetime` nos permite crear objetos de fecha especificando el año, el mes y el día. Cuando restamos una fecha de otra, Python devuelve un objeto `timedelta`. Podemos acceder al número de días en este objeto utilizando el atributo `.days`.

En este ejemplo, hay 64 días entre el 15 de enero de 2023 y el 20 de marzo de 2023.
