# Creando un Contenedor Personalizado - La Gran Ilusión

Almacenar los datos en columnas ofrece una mejor economía de memoria, pero ahora los datos son bastante extraños de trabajar. De hecho, ninguno de nuestro código de análisis anterior del Ejercicio 2.2 puede trabajar con columnas. La razón por la que todo está roto es que se ha roto la abstracción de datos que se utilizó en los ejercicios anteriores, a saber, la suposición de que los datos se almacenan como una lista de diccionarios.

Esto se puede corregir si está dispuesto a crear un objeto de contenedor personalizado que "haga la vista gorda". Hagámoslo.

El código de análisis anterior asume que los datos se almacenan en una secuencia de registros. Cada registro se representa como un diccionario. Comencemos creando una nueva clase "Secuencia". En esta clase, almacenaremos las cuatro columnas de datos que se usaban en la función `read_rides_as_columns()`.

```python
# readrides.py

from collections.abc import Sequence

...

class RideData(Sequence):
    def __init__(self):
        self.routes = []      # Columnas
        self.dates = []
        self.daytypes = []
        self.numrides = []
```

Intente crear una instancia de `RideData`. Verá que falla con un mensaje de error como este:

```python
>>> records = RideData()
Traceback (most recent call last):
...
TypeError: No se puede instanciar la clase abstracta RideData con métodos abstractos __getitem__, __len__
>>>
```

Lea detenidamente el mensaje de error. Nos dice lo que necesitamos implementar. Agreguemos un método `__len__()` y `__getitem__()`. En el método `__getitem__()`, crearemos un diccionario. Además, crearemos un método `append()` que tome un diccionario y lo desempaquete en 4 operaciones `append()` separadas.

```python
# readrides.py
...

class RideData(collections.Sequence):
    def __init__(self):
        # Cada valor es una lista con todos los valores (una columna)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # Se asume que todas las listas tienen la misma longitud
        return len(self.routes)

    def __getitem__(self, index):
        return { 'route': self.routes[index],
                 'date': self.dates[index],
                 'daytype': self.daytypes[index],
                 'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

Si lo ha hecho correctamente, debería poder insertar este objeto en la función `read_rides_as_dicts()` escrita anteriormente. Esto implica cambiar solo una línea de código:

```python
# readrides.py
...

def read_rides_as_dicts(filename):
    '''
    Lee los datos de viajes de autobús como una lista de dicts
    '''
    records = RideData()      # <--- CAMBIE ESTO
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Omite los encabezados
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides' : rides
                }
            records.append(record)
    return records
```

Si lo ha hecho bien, el código antiguo debería funcionar exactamente como antes. Por ejemplo:

```python
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> rows[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> rows[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>> rows[2]
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
>>>
```

Ejecute su código anterior de la CTA del Ejercicio 2.2. Debería funcionar sin modificar, pero utilizar significativamente menos memoria.
