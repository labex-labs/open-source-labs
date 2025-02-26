# Ejercicio 3.3: Lectura de archivos CSV

Para comenzar, centrémonos solo en el problema de leer un archivo CSV en una lista de diccionarios. En el archivo `fileparse_3.3.py`, defina una función que se vea así:

```python
# fileparse_3.3.py
import csv

def parse_csv(filename):
    '''
    Analiza un archivo CSV en una lista de registros
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Lee los encabezados del archivo
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Omite las filas sin datos
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

Esta función lee un archivo CSV en una lista de diccionarios mientras esconde los detalles de abrir el archivo, envolverlo con el módulo `csv`, ignorar las líneas en blanco, etc.

Prueba:

Pista: `python3 -i fileparse_3.3.py`.

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'}, {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'}, {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'}, {'name': 'IBM','shares': '100', 'price': '70.44'}]
>>>
```

Esto es bueno, excepto que no se pueden hacer ningún tipo de cálculo útil con los datos porque todo se representa como una cadena. Lo corregiremos pronto, pero sigamos construyendo sobre ello.
