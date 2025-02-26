# Übung 3.3: Lesen von CSV-Dateien

Zunächst konzentrieren wir uns nur auf das Problem, eine CSV-Datei in eine Liste von Dictionaries zu lesen. In der Datei `fileparse_3.3.py` definieren Sie eine Funktion, die wie folgt aussieht:

```python
# fileparse_3.3.py
import csv

def parse_csv(filename):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

Diese Funktion liest eine CSV-Datei in eine Liste von Dictionaries und versteckt dabei die Details des Dateiöffnens, der Umschließung mit dem `csv`-Modul, des Überspringens von leeren Zeilen usw.

Testen Sie es:

Hinweis: `python3 -i fileparse_3.3.py`.

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'}, {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'}, {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'}, {'name': 'IBM','shares': '100', 'price': '70.44'}]
>>>
```

Dies ist gut, nur dass Sie keine nützlichen Berechnungen mit den Daten durchführen können, da alles als String dargestellt ist. Wir werden das bald beheben, aber lassen Sie uns zunächst weiterbauen.
