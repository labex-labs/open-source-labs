# Revenons aux bases

Commencez par rétablir les modifications liées aux définitions de classes. Rewritez le fichier `reader.py` de sorte qu'il contienne les deux fonctions de base que vous aviez avant de la compliquer avec les classes :

```python
# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of instances
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

Vérifiez que le code fonctionne toujours comme avant :

```python
>>> import reader
>>> port = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
>>> port
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1},
 {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23},
 {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1},
 {'name': 'IBM','shares': 100, 'price': 70.44}]
>>> import stock
>>> port = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> port
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44),
 Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1),
 Stock('IBM', 100, 70.44)]
>>>
```
