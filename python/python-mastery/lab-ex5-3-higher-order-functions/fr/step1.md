# Utilisation de fonctions de haut niveau

À l'heure actuelle, le programme `reader.py` est composé de deux fonctions principales, `csv_as_dicts()` et `csv_as_instances()`. Le code dans ces deux fonctions est presque identique. Par exemple :

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convertit les lignes de données CSV en une liste de dictionnaires
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
    Convertit les lignes de données CSV en une liste d'instances
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

Unifie le noyau de ces fonctions en une seule fonction `convert_csv()` qui accepte une fonction de conversion définie par l'utilisateur en tant qu'argument. Par exemple :

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

Réécrivez les fonctions `csv_as_dicts()` et `csv_as_instances()` en fonction de la nouvelle fonction `convert_csv()`.
