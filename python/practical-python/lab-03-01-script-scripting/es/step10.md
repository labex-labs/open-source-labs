# Anotaciones de tipo

También puedes agregar sugerencias opcionales de tipo a las definiciones de funciones.

```python
def read_prices(filename: str) -> dict:
    '''
    Lee los precios de un archivo CSV con datos de nombre,precio
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

Las sugerencias no tienen ningún efecto operativo. Son puramente informativas. Sin embargo, pueden ser utilizadas por IDEs, verificadores de código y otras herramientas para hacer más.

En la sección 2, escribiste un programa llamado `report.py` que imprimía un informe mostrando el rendimiento de una cartera de acciones. Este programa consistía en algunas funciones. Por ejemplo:

```python
# report.py
import csv

def read_portfolio(filename):
    '''
    Lee un archivo de cartera de acciones en una lista de diccionarios con claves
    name, shares y price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
               'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)
    return portfolio
...
```

Sin embargo, también había porciones del programa que simplemente realizaban una serie de cálculos preestablecidos. Este código aparecía cerca del final del programa. Por ejemplo:

```python
...

# Imprime el informe

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 +'') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
...
```

En este ejercicio, vamos a tomar este programa y organizarlo un poco más sólidamente en torno al uso de funciones.
