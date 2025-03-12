# Creación de una clase de contenedor personalizada

En el procesamiento de datos, el enfoque orientado a columnas es excelente para ahorrar memoria. Sin embargo, puede causar problemas cuando tu código existente espera que los datos estén en forma de una lista de diccionarios. Para resolver este problema, crearemos una clase de contenedor personalizada. Esta clase presentará una interfaz orientada a filas, lo que significa que parecerá y actuará como una lista de diccionarios para tu código. Pero internamente, almacenará los datos en un formato orientado a columnas, lo que nos ayudará a ahorrar memoria.

1. Primero, abre el archivo `readrides.py` en el editor WebIDE. Vamos a agregar una nueva clase a este archivo. Esta clase será la base de nuestro contenedor personalizado.

```python
# Add this to readrides.py
from collections.abc import Sequence

class RideData(Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

En este código, definimos una clase llamada `RideData` que hereda de `Sequence`. El método `__init__` inicializa cuatro listas vacías, cada una representando una columna de datos. El método `__len__` devuelve la longitud del contenedor, que es la misma que la longitud de la lista `routes`. El método `__getitem__` nos permite acceder a un registro específico por índice, devolviéndolo como un diccionario. El método `append` agrega un nuevo registro al contenedor anexando valores a cada lista de columnas.

2. Ahora, necesitamos una función para leer los datos de viajes en autobús en nuestro contenedor personalizado. Agrega la siguiente función al archivo `readrides.py`.

```python
# Add this to readrides.py
def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts, but use our custom container
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

Esta función crea una instancia de la clase `RideData` y la llena con datos del archivo CSV. Lee cada fila del archivo, extrae la información relevante, crea un diccionario para cada registro y luego lo anexa al contenedor `RideData`. Lo importante es que mantiene la misma interfaz que una lista de diccionarios, pero internamente almacena los datos en columnas.

3. Probemos nuestro contenedor personalizado en la shell de Python. Esto nos ayudará a verificar que funciona como se espera.

```python
import readrides

# Read the data using our custom container
rows = readrides.read_rides_as_dicts('ctabus.csv')

# Check the type of the returned object
type(rows)  # Should be readrides.RideData

# Check the length
len(rows)   # Should be 577563

# Access individual records
rows[0]     # Should return a dictionary for the first record
rows[1]     # Should return a dictionary for the second record
rows[2]     # Should return a dictionary for the third record
```

Nuestro contenedor personalizado implementa con éxito la interfaz `Sequence`, lo que significa que se comporta como una lista. Puedes usar la función `len()` para obtener el número de registros en el contenedor, y puedes usar la indexación para acceder a registros individuales. Cada registro parece ser un diccionario, aunque los datos se almacenen internamente en columnas. Esto es genial porque el código existente que espera una lista de diccionarios seguirá funcionando con nuestro contenedor personalizado sin ninguna modificación.

4. Finalmente, midamos el uso de memoria de nuestro contenedor personalizado. Esto nos mostrará cuánta memoria estamos ahorrando en comparación con una lista de diccionarios.

```python
import tracemalloc

tracemalloc.start()
rows = readrides.read_rides_as_dicts('ctabus.csv')
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")
tracemalloc.stop()
```

Cuando ejecutes este código, deberías ver que el uso de memoria es similar al enfoque orientado a columnas, que es mucho menor que el que utilizaría una lista de diccionarios. Esto demuestra la ventaja de nuestro contenedor personalizado en términos de eficiencia de memoria.
