# Datos de primera clase

En el archivo `portfolio.csv`, leíste datos organizados en columnas que se ven así:

```python
"AA",100,32.20
"IBM",50,91.10
...
```

En el código anterior, estos datos se procesaron codificando todos los cambios de tipo. Por ejemplo:

```python
rows = csv.reader(f)
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

Este tipo de conversión también se puede realizar de manera más inteligente usando algunas operaciones de lista. Crea una lista de Python que contenga las conversiones que quieres realizar en cada columna:

```python
>>> coltypes = [str, int, float]
>>>
```

La razón por la que puedes incluso crear esta lista es que todo en Python es "de primera clase". Entonces, si quieres tener una lista de funciones, está bien.

Ahora, lee una fila de datos del archivo anterior:

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

Une los tipos de columna con la fila y mira el resultado:

```python
>>> r = list(zip(coltypes, row))
>>> r
[(<class'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>,'32.20')]
>>>
```

Notarás que esto ha emparejado una conversión de tipo con un valor. Por ejemplo, `int` se empareja con el valor `'100'`. Ahora, prueba esto:

```python
>>> record = [func(val) for func, val in zip(coltypes, row)]
>>> record
['AA', 100, 32.2]
>>>
```

Asegúrate de entender lo que está sucediendo en el código anterior. En el bucle, la variable `func` es una de las funciones de conversión de tipo (por ejemplo, `str`, `int`, etc.) y la variable `val` es uno de los valores como `'AA'`, `'100'`. La expresión `func(val)` está convirtiendo un valor (es como un casteo de tipo).

Puedes llevarlo un paso más y crear diccionarios usando los encabezados de columna. Por ejemplo:

```python
>>> dict(zip(headers, record))
{'name': 'AA','shares': 100, 'price': 32.2}
>>>
```

Si prefieres, puedes realizar todos estos pasos a la vez usando una comprensión de diccionario:

```python
>>> { name:func(val) for name, func, val in zip(headers, coltypes, row) }
{'name': 'AA','shares': 100, 'price': 32.2}
>>>
```
