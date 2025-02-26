# Uso de Memoria de Otras Estructuras de Datos

Python tiene muchas opciones diferentes para representar estructuras de datos. Por ejemplo:

```python
# Una tupla
row = (route, date, daytype, rides)

# Un diccionario
row = {
    'route': route,
    'date': date,
    'daytype': daytype,
    'rides': rides,
}

# Una clase
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# Una tupla con nombres
from collections import namedtuple
Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

# Una clase con __slots__
class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
```

Su tarea es la siguiente: Cree diferentes versiones de la función `read_rides()` que usen cada una de estas estructuras de datos para representar una sola fila de datos. Luego, determine el uso de memoria resultante de cada opción. Encuentre qué enfoque ofrece el almacenamiento más eficiente si estuviera trabajando con una gran cantidad de datos a la vez.
