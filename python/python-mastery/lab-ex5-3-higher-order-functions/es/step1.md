# Usando funciones de orden superior

En este momento, el programa `reader.py` consta de dos funciones principales, `csv_as_dicts()` y `csv_as_instances()`. El código en estas dos funciones es casi idéntico. Por ejemplo:

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convertir líneas de datos CSV en una lista de diccionarios
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = { name: func(val)
                   for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convertir líneas de datos CSV en una lista de instancias
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records
```

Unificar el núcleo de estas funciones en una sola función `convert_csv()` que acepte una función de conversión definida por el usuario como argumento. Por ejemplo:

```python
>>> def make_dict(headers, row):
        return dict(zip(headers, row))

>>> lines = open('portfolio.csv')
>>> convert_csv(lines, make_dict)
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'},
 {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'},
 {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'},
 {'name': 'IBM','shares': '100', 'price': '70.44'}]
>>>
```

Reescribir las funciones `csv_as_dicts()` y `csv_as_instances()` en términos de la nueva función `convert_csv()`.
