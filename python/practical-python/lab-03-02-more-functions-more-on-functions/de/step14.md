# Übung 3.4: Erstellen eines Spaltenauswahlers

In vielen Fällen interessieren Sie sich nur für ausgewählte Spalten aus einer CSV-Datei, nicht für alle Daten. Ändern Sie die `parse_csv()`-Funktion so, dass sie optional erlaubt, dass Benutzerangegebene Spalten ausgewählt werden, wie folgt:

```python
>>> # Lese alle Daten
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'}, {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'}, {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'}, {'name': 'IBM','shares': '100', 'price': '70.44'}]

>>> # Lese nur einige Daten
>>> shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares'])
>>> shares_held
[{'name': 'AA','shares': '100'}, {'name': 'IBM','shares': '50'}, {'name': 'CAT','shares': '150'}, {'name': 'MSFT','shares': '200'}, {'name': 'GE','shares': '95'}, {'name': 'MSFT','shares': '50'}, {'name': 'IBM','shares': '100'}]
>>>
```

Ein Beispiel für einen Spaltenauswähler wurde in Übung 2.23 gegeben. Hier ist jedoch eine Möglichkeit, dies zu tun:

```python
# fileparse_3.4.py
import csv

def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Lese die Dateiheader
        headers = next(rows)

        # Wenn ein Spaltenauswähler angegeben wurde, finde die Indizes der angegebenen Spalten.
        # Vereng auch die Menge der Header, die für die resultierenden Dictionaries verwendet werden
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Überspringe Zeilen ohne Daten
                continue
            # Filtere die Zeile, wenn spezifische Spalten ausgewählt wurden
            if indices:
                row = [ row[index] for index in indices ]

            # Mache ein Dictionary
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

Es gibt einige knifflige Punkte bei diesem Teil. Wahrscheinlich der wichtigste ist die Zuordnung der Spaltenauswahlen zu Zeilenindizes. Beispielsweise nehmen Sie an, die Eingabedatei hätte die folgenden Header:

```python
>>> headers = ['name', 'date', 'time','shares', 'price']
>>>
```

Nun nehmen Sie an, die ausgewählten Spalten wären wie folgt:

```python
>>> select = ['name','shares']
>>>
```

Um die richtige Auswahl durchzuführen, müssen Sie die ausgewählten Spaltennamen auf die Spaltenindizes in der Datei abbilden. Dies ist, was dieser Schritt tut:

```python
>>> indices = [headers.index(colname) for colname in select ]
>>> indices
[0, 3]
>>>
```

Mit anderen Worten, "name" ist Spalte 0 und "shares" ist Spalte 3. Wenn Sie eine Zeile von Daten aus der Datei lesen, werden die Indizes verwendet, um sie zu filtern:

```python
>>> row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
>>> row = [ row[index] for index in indices ]
>>> row
['AA', '100']
>>>
```
