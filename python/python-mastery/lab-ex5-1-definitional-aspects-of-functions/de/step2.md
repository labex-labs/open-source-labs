# Erstellen der grundlegenden CSV-Reader-Funktionen

Beginnen wir damit, eine `reader.py`-Datei mit zwei grundlegenden Funktionen zum Lesen von CSV-Daten zu erstellen. Diese Funktionen werden uns helfen, CSV-Dateien auf verschiedene Weise zu verarbeiten, wie z. B. die Daten in Dictionaries oder Klasseninstanzen umzuwandeln.

Zunächst müssen wir verstehen, was eine CSV-Datei ist. CSV steht für Comma-Separated Values (Komma-getrennte Werte). Es ist ein einfaches Dateiformat, das zur Speicherung tabellarischer Daten verwendet wird, wobei jede Zeile eine Zeile darstellt und die Werte in jeder Zeile durch Kommas getrennt sind.

Jetzt erstellen wir die `reader.py`-Datei. Befolgen Sie diese Schritte:

1. Öffnen Sie den Code-Editor und erstellen Sie eine neue Datei namens `reader.py` im Verzeichnis `/home/labex/project`. Hier werden wir unsere Funktionen zum Lesen von CSV-Daten schreiben.

2. Fügen Sie den folgenden Code in die `reader.py`-Datei ein:

```python
# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
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
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
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

In der `read_csv_as_dicts`-Funktion öffnen wir zunächst die CSV-Datei mit der `open`-Funktion. Dann verwenden wir die `csv.reader`-Funktion, um die Datei Zeile für Zeile zu lesen. Die Anweisung `next(rows)` liest die erste Zeile der Datei, die normalerweise die Kopfzeilen enthält. Danach iterieren wir über die verbleibenden Zeilen. Für jede Zeile erstellen wir ein Dictionary, bei dem die Schlüssel die Kopfzeilen sind und die Werte die entsprechenden Werte in der Zeile sind, mit optionaler Typkonvertierung mithilfe der `types`-Liste.

Die `read_csv_as_instances`-Funktion ist ähnlich, erstellt jedoch anstelle von Dictionaries Instanzen einer gegebenen Klasse. Sie geht davon aus, dass die Klasse eine statische Methode namens `from_row` hat, die eine Instanz aus einer Datenzeile erstellen kann.

3. Testen wir diese Funktionen, um sicherzustellen, dass sie korrekt funktionieren. Erstellen Sie eine neue Datei namens `test_reader.py` mit dem folgenden Code:

```python
# test_reader.py

import reader
import stock

# Test reading CSV as dictionaries
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First portfolio item as dictionary:", portfolio_dicts[0])
print("Total items:", len(portfolio_dicts))

# Test reading CSV as class instances
portfolio_instances = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst portfolio item as Stock instance:", portfolio_instances[0])
print("Total items:", len(portfolio_instances))
```

In der `test_reader.py`-Datei importieren wir das `reader`-Modul, das wir gerade erstellt haben, und das `stock`-Modul. Dann testen wir die beiden Funktionen, indem wir sie mit einer Beispiel-CSV-Datei namens `portfolio.csv` aufrufen. Wir geben das erste Element und die Gesamtzahl der Elemente im Portfolio aus, um zu überprüfen, ob die Funktionen wie erwartet funktionieren.

4. Führen Sie das Testskript aus dem Terminal aus:

```bash
python test_reader.py
```

Die Ausgabe sollte in etwa so aussehen:

```
First portfolio item as dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First portfolio item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7
```

Dies bestätigt, dass unsere beiden Funktionen korrekt funktionieren. Die erste Funktion wandelt CSV-Daten in eine Liste von Dictionaries mit korrekter Typkonvertierung um, und die zweite Funktion erstellt Klasseninstanzen mithilfe einer statischen Methode der angegebenen Klasse.

Im nächsten Schritt werden wir diese Funktionen refaktorisieren, um sie flexibler zu machen, indem wir es ihnen ermöglichen, mit jeder iterierbaren Datenquelle zu arbeiten, nicht nur mit Dateinamen.
