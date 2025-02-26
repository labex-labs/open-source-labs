# Übung 2.23: Extrahieren von Daten aus CSV-Dateien

Das Wissen, wie verschiedene Kombinationen von Listen-, Mengen- und Wörterbuchverständnissen verwendet werden können, kann in verschiedenen Formen der Datenverarbeitung nützlich sein. Hier ist ein Beispiel, das zeigt, wie man ausgewählte Spalten aus einer CSV-Datei extrahiert.

Zunächst lesen Sie eine Zeile mit Header-Informationen aus einer CSV-Datei:

```python
>>> import csv
>>> f = open('portfoliodate.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'date', 'time','shares', 'price']
>>>
```

Als nächstes definieren Sie eine Variable, die die Spalten auflistet, die Sie tatsächlich interessieren:

```python
>>> select = ['name','shares', 'price']
>>>
```

Legen Sie nun die Indizes der obigen Spalten in der Quell-CSV-Datei fest:

```python
>>> indices = [ headers.index(colname) for colname in select ]
>>> indices
[0, 3, 4]
>>>
```

Schließlich lesen Sie eine Zeile von Daten und wandeln sie mithilfe eines Wörterbuchverständnisses in ein Wörterbuch um:

```python
>>> row = next(rows)
>>> record = { colname: row[index] for colname, index in zip(select, indices) }   # dict-comprehension
>>> record
{'price': '32.20', 'name': 'AA','shares': '100'}
>>>
```

Wenn Sie sich mit dem, was gerade passiert ist, wohlfühlen, lesen Sie den Rest der Datei:

```python
>>> portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
>>> portfolio
[{'price': '91.10', 'name': 'IBM','shares': '50'}, {'price': '83.44', 'name': 'CAT','shares': '150'},
  {'price': '51.23', 'name': 'MSFT','shares': '200'}, {'price': '40.37', 'name': 'GE','shares': '95'},
  {'price': '65.10', 'name': 'MSFT','shares': '50'}, {'price': '70.44', 'name': 'IBM','shares': '100'}]
>>>
```

Oh je, Sie haben gerade einen Großteil der `read_portfolio()`-Funktion auf eine einzelne Anweisung reduziert.
