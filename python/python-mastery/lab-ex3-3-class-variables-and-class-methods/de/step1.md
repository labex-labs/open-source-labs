# Vorheriges Labor

Instanzen der Klasse `Stock`, die im vorherigen Labor definiert wurde, werden normalerweise wie folgt erstellt:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>>
```

Die Funktion `read_portfolio()`, erstellt jedoch auch Instanzen aus Zeilen von Daten, die aus Dateien gelesen werden. Beispielsweise wird Code wie der folgende verwendet:

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> s = Stock(row[0], int(row[1]), float(row[2]))
>>>
```
