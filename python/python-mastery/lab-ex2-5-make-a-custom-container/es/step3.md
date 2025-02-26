# Cambiando su Orientación (a Columnas)

A menudo puede ahorrar mucha memoria si cambia su forma de ver los datos. Por ejemplo, ¿qué pasa si lee todos los datos del autobús en columnas utilizando esta función?

```python
# readrides.py

...

def read_rides_as_columns(filename):
    '''
    Lee los datos de viajes de autobús en 4 listas, que representan columnas
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Omite los encabezados
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

En teoría, esta función debería ahorrar mucha memoria. Analicémosla antes de probarla.

Primero, el archivo de datos contenía 577563 filas de datos donde cada fila contenía cuatro valores. Si cada fila se almacena como un diccionario, entonces esos diccionarios tienen un tamaño mínimo de 240 bytes.

```python
>>> nrows = 577563     # Número de filas en el archivo original
>>> nrows * 240
138615120
>>>
```

Entonces, solo para los diccionarios en sí son 138MB. Esto no incluye ninguno de los valores realmente almacenados en los diccionarios.

Al cambiar a columnas, los datos se almacenan en 4 listas separadas.\
Cada lista requiere 8 bytes por elemento para almacenar un puntero. Entonces, aquí está una estimación aproximada de los requisitos de la lista:

```python
>>> nrows * 4 * 8
18482016
>>>
```

Eso es aproximadamente 18MB en sobrecarga de lista. Entonces, cambiar a una orientación de columnas debería ahorrar aproximadamente 120MB de memoria solo al eliminar toda la información adicional que necesita ser almacenada en diccionarios.

Intente usar esta función para leer los datos del autobús y ver el uso de memoria.

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> columns = read_rides_as_columns('ctabus.csv')
>>> tracemalloc.get_traced_memory()
... mira el resultado...
>>>
```

¿El resultado refleja los ahorros en memoria esperados a partir de nuestros cálculos aproximados anteriores?
