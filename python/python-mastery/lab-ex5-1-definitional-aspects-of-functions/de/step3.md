# Über Flexibilität nachdenken

Derzeit sind die beiden Funktionen in `reader.py` so programmiert, dass sie mit Dateinamen arbeiten, die direkt an `open()` übergeben werden. Refaktorieren Sie den Code, sodass er mit jedem iterierbaren Objekt funktioniert, das Zeilen erzeugt. Dazu erstellen Sie zwei neue Funktionen `csv_as_dicts(lines, types)` und `csv_as_instances(lines, cls)`, die jede iterierbare Zeilensequenz umwandeln. Beispielsweise:

```python
>>> file = open('portfolio.csv')
>>> port = reader.csv_as_dicts(file, [str, int, float])
>>> port
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1},
 {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23},
 {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1},
 {'name': 'IBM','shares': 100, 'price': 70.44}]
>>>
```

Der ganze Grund dafür, dies zu tun, ist es, es möglich zu machen, mit verschiedenen Arten von Eingabesourcen zu arbeiten. Beispielsweise:

```python
>>> import gzip
>>> import stock
>>> file = gzip.open('portfolio.csv.gz')
>>> port = reader.csv_as_instances(file, stock.Stock)
>>> port
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44),
 Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1),
 Stock('IBM', 100, 70.44)]
>>>
```

Um die Rückwärtskompatibilität zu älteren Code zu gewährleisten, schreiben Sie die Funktionen `read_csv_as_dicts()` und `read_csv_as_instances()`, die wie zuvor einen Dateinamen entgegennehmen. Diese Funktionen sollten `open()` auf dem übergebenen Dateinamen aufrufen und die neuen `csv_as_dicts()`- oder `csv_as_instances()`-Funktionen auf der resultierenden Datei verwenden.
