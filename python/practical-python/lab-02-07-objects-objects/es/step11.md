# Ejercicio 2.24: Datos de primer clase

En el archivo `portfolio.csv`, leemos datos organizados en columnas que se ven así:

```csv
name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
```

En el código anterior, usamos el módulo `csv` para leer el archivo, pero todavía tuvimos que realizar conversiones de tipo manuales. Por ejemplo:

```python
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

Este tipo de conversión también se puede realizar de manera más inteligente usando algunas operaciones básicas de listas.

Crea una lista de Python que contenga los nombres de las funciones de conversión que usarías para convertir cada columna en el tipo adecuado:

```python
>>> types = [str, int, float]
>>>
```

La razón por la que puedes incluso crear esta lista es que todo en Python es _de primer clase_. Entonces, si quieres tener una lista de funciones, está bien. Los elementos de la lista que creaste son funciones para convertir un valor `x` en un tipo dado (por ejemplo, `str(x)`, `int(x)`, `float(x)`).

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

Como se mencionó, esta fila no es suficiente para hacer cálculos porque los tipos son incorrectos. Por ejemplo:

```python
>>> row[1] * row[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type'str'
>>>
```

Sin embargo, quizás los datos se pueden emparejar con los tipos que especificaste en `types`. Por ejemplo:

```python
>>> types[1]
<type 'int'>
>>> row[1]
'100'
>>>
```

Intenta convertir uno de los valores:

```python
>>> types[1](row[1])     # Lo mismo que int(row[1])
100
>>>
```

Intenta convertir un valor diferente:

```python
>>> types[2](row[2])     # Lo mismo que float(row[2])
32.2
>>>
```

Intenta el cálculo con los valores convertidos:

```python
>>> types[1](row[1])*types[2](row[2])
3220.0000000000005
>>>
```

Empareja los tipos de columna con los campos y mira el resultado:

```python
>>> r = list(zip(types, row))
>>> r
[(<type'str'>, 'AA'), (<type 'int'>, '100'), (<type 'float'>,'32.20')]
>>>
```

Notarás que esto ha emparejado una conversión de tipo con un valor. Por ejemplo, `int` se empareja con el valor `'100'`.

La lista emparejada es útil si quieres realizar conversiones en todos los valores, uno después del otro. Prueba esto:

```python
>>> converted = []
>>> for func, val in zip(types, row):
          converted.append(func(val))
...
>>> converted
['AA', 100, 32.2]
>>> converted[1] * converted[2]
3220.0000000000005
>>>
```

Asegúrate de entender lo que está sucediendo en el código anterior. En el bucle, la variable `func` es una de las funciones de conversión de tipo (por ejemplo, `str`, `int`, etc.) y la variable `val` es uno de los valores como `'AA'`, `'100'`. La expresión `func(val)` está convirtiendo un valor (parecido a un casteo de tipo).

El código anterior se puede comprimir en una sola comprensión de lista.

```python
>>> converted = [func(val) for func, val in zip(types, row)]
>>> converted
['AA', 100, 32.2]
>>>
```
