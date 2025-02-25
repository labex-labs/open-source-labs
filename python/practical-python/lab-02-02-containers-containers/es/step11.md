# Ejercicio 2.6: Diccionarios como contenedor

Un diccionario es una forma útil de mantener un registro de elementos cuando se desea buscar elementos utilizando un índice diferente de un entero. En la shell de Python, intenta jugar con un diccionario:

```python
>>> prices = { }
>>> prices['IBM'] = 92.45
>>> prices['MSFT'] = 45.12
>>> prices
... mira el resultado...
>>> prices['IBM']
92.45
>>> prices['AAPL']
... mira el resultado...
>>> 'AAPL' in prices
False
>>>
```

El archivo `prices.csv` contiene una serie de líneas con los precios de las acciones. El archivo se parece a esto:

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
"C",3.72
...
```

Escribe una función `read_prices(filename)` que lea un conjunto de precios como este en un diccionario donde las claves del diccionario son los nombres de las acciones y los valores en el diccionario son los precios de las acciones.

Para hacer esto, comienza con un diccionario vacío y comienza a insertar valores en él exactamente como lo hiciste anteriormente. Sin embargo, ahora estás leyendo los valores de un archivo.

Utilizaremos esta estructura de datos para buscar rápidamente el precio de un nombre de acción dado.

Unos pocos consejos que necesitarás para esta parte. Primero, asegúrate de usar el módulo `csv` como lo hiciste antes: no es necesario reinventar la rueda aquí.

```python
>>> import csv
>>> f = open('/home/labex/project/prices.csv', 'r')
>>> rows = csv.reader(f)
>>> for row in rows:
        print(row)


['AA', '9.22']
['AXP', '24.85']
...
[]
>>>
```

La otra pequeña complicación es que el archivo `prices.csv` puede tener algunas líneas en blanco. Observa cómo la última fila de datos arriba es una lista vacía, lo que significa que no había datos en esa línea.

Es posible que esto cause que tu programa se detenga con una excepción. Utiliza las declaraciones `try` y `except` para capturar esto adecuadamente. Pensamiento: ¿sería mejor protegerse contra datos incorrectos con una declaración `if` en lugar de eso?

Una vez que hayas escrito tu función `read_prices()`, pruébalo de forma interactiva para asegurarte de que funcione:

```python
>>> prices = read_prices('/home/labex/project/prices.csv')
>>> prices['IBM']
106.28
>>> prices['MSFT']
20.89
>>>
```
