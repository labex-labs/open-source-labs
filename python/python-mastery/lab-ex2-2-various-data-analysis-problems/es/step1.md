# Preliminares

Para comenzar, repasemos algunos conceptos básicos con un conjunto de datos un poco más simple: una cartera de inversiones en acciones. Crea un archivo `readport.py` y pon este código en él:

```python
# readport.py

import csv

# Una función que lee un archivo y lo convierte en una lista de diccionarios
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
               'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

Este archivo lee algunos datos simples del mercado de valores en el archivo `portfolio.csv`. Utiliza la función para leer el archivo y mira los resultados:

Abre una shell de Python y prueba lo siguiente:

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2,'shares': 100},
 {'name': 'IBM', 'price': 91.1,'shares': 50},
 {'name': 'CAT', 'price': 83.44,'shares': 150},
 {'name': 'MSFT', 'price': 51.23,'shares': 200},
 {'name': 'GE', 'price': 40.37,'shares': 95},
 {'name': 'MSFT', 'price': 65.1,'shares': 50},
 {'name': 'IBM', 'price': 70.44,'shares': 100}]
>>>
```

En estos datos, cada fila consta del nombre de una acción, la cantidad de acciones poseídas y el precio de compra. Hay múltiples entradas para ciertos nombres de acciones como MSFT e IBM.
