# Ejercicio 2.4: Una lista de tuplas

El archivo `portfolio.csv` contiene una lista de acciones en un portafolio. En el Ejercicio 1.30, escribiste una función `portfolio_cost(filename)` que leía este archivo y realizaba un cálculo simple.

Tu código debería haber sido algo así:

```python
# pcost.py

import csv

def portfolio_cost(filename):
    '''Calcula el costo total (acciones*precio) de un archivo de portafolio'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
```

Usando este código como guía aproximada, crea un nuevo archivo `report.py`. En ese archivo, define una función `read_portfolio(filename)` que abre un archivo de portafolio dado y lo lee en una lista de tuplas. Para hacer esto, vas a hacer algunos cambios menores al código anterior.

Primero, en lugar de definir `total_cost = 0`, crearás una variable que inicialmente se establece en una lista vacía. Por ejemplo:

```python
portfolio = []
```

Luego, en lugar de sumar el costo, convertirás cada fila en una tupla exactamente como lo hiciste en el último ejercicio y la agregará a esta lista. Por ejemplo:

```python
for row in rows:
    holding = (row[0], int(row[1]), float(row[2]))
    portfolio.append(holding)
```

Finalmente, devolverás la lista `portfolio` resultante.

Experimenta con tu función de forma interactiva (simplemente un recordatorio de que para hacer esto, primero debes ejecutar el programa `report.py` en el intérprete):

_Consejo: Utiliza `-i` cuando ejecutes el archivo en la terminal_

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[('AA', 100, 32.2), ('IBM', 50, 91.1), ('CAT', 150, 83.44), ('MSFT', 200, 51.23),
    ('GE', 95, 40.37), ('MSFT', 50, 65.1), ('IBM', 100, 70.44)]
>>>
>>> portfolio[0]
('AA', 100, 32.2)
>>> portfolio[1]
('IBM', 50, 91.1)
>>> portfolio[1][1]
50
>>> total = 0.0
>>> for s in portfolio:
        total += s[1] * s[2]

>>> print(total)
44671.15
>>>
```

Esta lista de tuplas que has creado es muy similar a una matriz bidimensional. Por ejemplo, puedes acceder a una columna y fila específicas usando una búsqueda como `portfolio[row][column]` donde `row` y `column` son enteros.

Dicho esto, también puedes reescribir el último bucle for usando una declaración como esta:

```python
>>> total = 0.0
>>> for name, shares, price in portfolio:
            total += shares*price

>>> print(total)
44671.15
>>>
```
