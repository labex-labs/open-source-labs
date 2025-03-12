# Uso de las funciones `enumerate()` y `zip()`

En este paso, exploraremos dos funciones integradas (built - in) en Python increíblemente útiles que son esenciales para la iteración: `enumerate()` y `zip()`. Estas funciones pueden simplificar significativamente tu código cuando trabajas con secuencias.

## Contando con `enumerate()`

Cuando estás iterando sobre una secuencia, a menudo es necesario llevar un registro del índice o posición de cada elemento. Ahí es donde la función `enumerate()` resulta útil. La función `enumerate()` toma una secuencia como entrada y devuelve pares de (índice, valor) para cada elemento de esa secuencia.

Si has estado siguiendo en el intérprete de Python del paso anterior, puedes continuar usando el mismo. De lo contrario, inicia una nueva sesión. Aquí te mostramos cómo configurar los datos si estás comenzando desde cero:

```python
# If you're starting a new session, reload the data first:
# import csv
# f = open('portfolio.csv')
# f_csv = csv.reader(f)
# headers = next(f_csv)
# rows = list(f_csv)

# Use enumerate to get row numbers
for rowno, row in enumerate(rows):
    print(rowno, row)
```

Cuando ejecutas el código anterior, la función `enumerate(rows)` generará pares de un índice (comenzando desde 0) y la fila correspondiente de la secuencia `rows`. Luego, el bucle `for` desempaqueta estos pares en las variables `rowno` y `row`, y los imprimimos.

Salida:

```
0 ['AA', '100', '32.20']
1 ['IBM', '50', '91.10']
2 ['CAT', '150', '83.44']
3 ['MSFT', '200', '51.23']
4 ['GE', '95', '40.37']
5 ['MSFT', '50', '65.10']
6 ['IBM', '100', '70.44']
```

Podemos hacer que el código sea aún más legible combinando `enumerate()` con el desempaquetado. El desempaquetado nos permite asignar directamente los elementos de una secuencia a variables individuales.

```python
for rowno, (name, shares, price) in enumerate(rows):
    print(rowno, name, shares, price)
```

En este código, estamos usando un par adicional de paréntesis alrededor de `(name, shares, price)` para desempaquetar correctamente los datos de la fila. `enumerate(rows)` sigue dándonos el índice y la fila, pero ahora estamos desempaquetando la fila en las variables `name`, `shares` y `price`.

Salida:

```
0 AA 100 32.20
1 IBM 50 91.10
2 CAT 150 83.44
3 MSFT 200 51.23
4 GE 95 40.37
5 MSFT 50 65.10
6 IBM 100 70.44
```

## Emparejando datos con `zip()`

La función `zip()` es otra herramienta poderosa en Python. Se utiliza para combinar elementos correspondientes de múltiples secuencias. Cuando pasas múltiples secuencias a `zip()`, crea un iterador que produce tuplas, donde cada tupla contiene elementos de cada una de las secuencias de entrada en la misma posición.

Veamos cómo podemos usar `zip()` con los datos de `headers` y `row` con los que hemos estado trabajando.

```python
# Recall the headers variable from earlier
print(headers)  # Should show ['name', 'shares', 'price']

# Get the first row
row = rows[0]
print(row)      # Should show ['AA', '100', '32.20']

# Use zip to pair column names with values
for col, val in zip(headers, row):
    print(col, val)
```

En este código, `zip(headers, row)` toma la secuencia `headers` y la secuencia `row` y empareja sus elementos correspondientes. Luego, el bucle `for` desempaqueta estos pares en `col` (para el nombre de la columna de `headers`) y `val` (para el valor de `row`), y los imprimimos.

Salida:

```
['name', 'shares', 'price']
['AA', '100', '32.20']
name AA
shares 100
price 32.20
```

Un uso muy común de `zip()` es crear diccionarios a partir de pares clave - valor. En Python, un diccionario es una colección de pares clave - valor.

```python
# Create a dictionary from headers and row values
record = dict(zip(headers, row))
print(record)
```

Aquí, `zip(headers, row)` crea pares de nombres de columnas y valores, y la función `dict()` toma estos pares y los convierte en un diccionario.

Salida:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
```

Podemos extender esta idea para convertir todas las filas de nuestra secuencia `rows` en diccionarios.

```python
# Convert all rows to dictionaries
for row in rows:
    record = dict(zip(headers, row))
    print(record)
```

En este bucle, para cada fila en `rows`, usamos `zip(headers, row)` para crear pares clave - valor y luego `dict()` para convertir esos pares en un diccionario. Esta técnica es muy común en aplicaciones de procesamiento de datos, especialmente cuando se trabaja con archivos CSV donde la primera fila contiene encabezados.

Salida:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'IBM', 'shares': '50', 'price': '91.10'}
{'name': 'CAT', 'shares': '150', 'price': '83.44'}
{'name': 'MSFT', 'shares': '200', 'price': '51.23'}
{'name': 'GE', 'shares': '95', 'price': '40.37'}
{'name': 'MSFT', 'shares': '50', 'price': '65.10'}
{'name': 'IBM', 'shares': '100', 'price': '70.44'}
```
