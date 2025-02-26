# Verwendung von Higher-Order-Funktionen

Derzeit besteht das Programm `reader.py` aus zwei Kernfunktionen, `csv_as_dicts()` und `csv_as_instances()`. Der Code in diesen beiden Funktionen ist fast identisch. Beispielsweise:

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Konvertiert Zeilen von CSV-Daten in eine Liste von Dictionaries
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
    Konvertiert Zeilen von CSV-Daten in eine Liste von Instanzen
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

Vereinige den Kern dieser Funktionen in eine einzelne Funktion `convert_csv()`, die eine benutzerdefinierte Konversionsfunktion als Argument akzeptiert. Beispielsweise:

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

Schreiben Sie die Funktionen `csv_as_dicts()` und `csv_as_instances()` in Bezug auf die neue Funktion `convert_csv()`.
