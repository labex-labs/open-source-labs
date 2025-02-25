# Ejercicio 1.33: Leyendo desde la línea de comandos

En el programa `pcost.py`, el nombre del archivo de entrada se ha fijado en el código:

```python
# pcost.py

def portfolio_cost(filename):
 ...
    # Su código aquí
 ...

cost = portfolio_cost('portfolio.csv')
print('Total cost:', cost)
```

Eso está bien para aprender y probar, pero en un programa real probablemente no harías eso.

En cambio, es posible que pasaras el nombre del archivo como argumento a un script. Intenta cambiar la parte inferior del programa de la siguiente manera:

```python
# pcost_1.33.py

import csv


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)  # Omite la fila de encabezados
        for row in rows:
            if len(row) < 3:
                print("Saltando fila no válida:", row)
                continue
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except (IndexError, ValueError):
                print("Saltando fila no válida:", row)

    return total_cost

import sys


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
```

`sys.argv` es una lista que contiene los argumentos pasados en la línea de comandos (si los hay).

Para ejecutar su programa, tendrás que ejecutar Python desde la terminal.

Por ejemplo, desde bash en Unix:

```bash
$ python3 pcost.py portfolio.csv
Total cost: 44671.15
bash %
```
