# Ejercicio 3.4: Construyendo un selector de columnas

En muchos casos, solo estás interesado en columnas seleccionadas de un archivo CSV, no en todos los datos. Modifica la función `parse_csv()` de modo que opcionalmente permita que se seleccionen columnas especificadas por el usuario de la siguiente manera:

```python
>>> # Lee todos los datos
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'}, {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'}, {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'}, {'name': 'IBM','shares': '100', 'price': '70.44'}]

>>> # Lee solo algunos de los datos
>>> shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares'])
>>> shares_held
[{'name': 'AA','shares': '100'}, {'name': 'IBM','shares': '50'}, {'name': 'CAT','shares': '150'}, {'name': 'MSFT','shares': '200'}, {'name': 'GE','shares': '95'}, {'name': 'MSFT','shares': '50'}, {'name': 'IBM','shares': '100'}]
>>>
```

Un ejemplo de selector de columnas se dio en el Ejercicio 2.23. Sin embargo, aquí está una forma de hacerlo:

```python
# fileparse_3.4.py
import csv

def parse_csv(filename, select=None):
    '''
    Analiza un archivo CSV en una lista de registros
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Lee los encabezados del archivo
        headers = next(rows)

        # Si se dio un selector de columnas, encuentra los índices de las columnas especificadas.
        # También restringe el conjunto de encabezados utilizado para los diccionarios resultantes
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Omite las filas sin datos
                continue
            # Filtra la fila si se seleccionaron columnas específicas
            if indices:
                row = [ row[index] for index in indices ]

            # Crea un diccionario
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

Hay varios aspectos complicados en esta parte. Probablemente el más importante es la asignación de las selecciones de columnas a los índices de fila. Por ejemplo, suponga que el archivo de entrada tuviera los siguientes encabezados:

```python
>>> headers = ['name', 'date', 'time','shares', 'price']
>>>
```

Ahora, suponga que las columnas seleccionadas fueran las siguientes:

```python
>>> select = ['name','shares']
>>>
```

Para realizar la selección adecuada, tienes que asignar los nombres de columnas seleccionados a los índices de columna en el archivo. Eso es lo que hace este paso:

```python
>>> indices = [headers.index(colname) for colname in select ]
>>> indices
[0, 3]
>>>
```

En otras palabras, "name" es la columna 0 y "shares" es la columna 3. Cuando lees una fila de datos del archivo, los índices se utilizan para filtrarla:

```python
>>> row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
>>> row = [ row[index] for index in indices ]
>>> row
['AA', '100']
>>>
```
