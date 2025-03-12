# Machbarkeit der Funktionen erhöhen

Derzeit sind unsere Funktionen darauf beschränkt, aus Dateien zu lesen, die durch einen Dateinamen angegeben werden. Dies schränkt ihre Anwendbarkeit ein. In der Programmierung ist es oft vorteilhaft, Funktionen flexibler zu gestalten, damit sie verschiedene Arten von Eingaben verarbeiten können. In unserem Fall wäre es toll, wenn unsere Funktionen mit jedem iterierbaren Objekt arbeiten könnten, das Zeilen erzeugt, wie z. B. Dateiobjekte oder andere Datenquellen. So können wir diese Funktionen in mehr Szenarien verwenden, wie z. B. das Lesen aus komprimierten Dateien oder anderen Datenströmen.

Lassen Sie uns unseren Code refaktorisieren, um diese Flexibilität zu ermöglichen:

1. Öffnen Sie die `reader.py`-Datei. Wir werden sie ändern, um einige neue Funktionen hinzuzufügen. Diese neuen Funktionen ermöglichen es unserem Code, mit verschiedenen Arten von iterierbaren Objekten zu arbeiten. Hier ist der Code, den Sie hinzufügen müssen:

```python
# reader.py

import csv

def csv_as_dicts(lines, types):
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls):
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types)

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)
```

Schauen wir uns genauer an, wie wir den Code refaktoriert haben:

1. Wir haben zwei allgemeinere Funktionen, `csv_as_dicts()` und `csv_as_instances()`, erstellt. Diese Funktionen sind so konzipiert, dass sie mit jedem iterierbaren Objekt arbeiten können, das CSV-Zeilen erzeugt. Das bedeutet, dass sie verschiedene Arten von Eingabequellen verarbeiten können, nicht nur Dateien, die durch einen Dateinamen angegeben werden.
2. Wir haben `read_csv_as_dicts()` und `read_csv_as_instances()` neu implementiert, um diese neuen Funktionen zu verwenden. Auf diese Weise ist die ursprüngliche Funktionalität des Lesens aus einer Datei über den Dateinamen weiterhin verfügbar, aber jetzt basiert sie auf den flexibleren Funktionen.
3. Dieser Ansatz gewährleistet die Rückwärtskompatibilität mit bestehendem Code. Das bedeutet, dass jeder Code, der die alten Funktionen verwendet hat, weiterhin wie erwartet funktioniert. Gleichzeitig wird unsere Bibliothek flexibler, da sie jetzt verschiedene Arten von Eingabequellen verarbeiten kann.

4. Jetzt testen wir diese neuen Funktionen. Erstellen Sie eine Datei namens `test_reader_flexibility.py` und fügen Sie den folgenden Code hinzu. Dieser Code wird die neuen Funktionen mit verschiedenen Arten von Eingabequellen testen:

```python
# test_reader_flexibility.py

import reader
import stock
import gzip

# Test opening a regular file
with open('portfolio.csv') as file:
    portfolio = reader.csv_as_dicts(file, [str, int, float])
    print("First item from open file:", portfolio[0])

# Test opening a gzipped file
with gzip.open('portfolio.csv.gz', 'rt') as file:  # 'rt' means read text
    portfolio = reader.csv_as_instances(file, stock.Stock)
    print("\nFirst item from gzipped file:", portfolio[0])

# Test backward compatibility
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item using backward compatible function:", portfolio[0])
```

3. Nachdem Sie die Testdatei erstellt haben, müssen Sie das Testskript aus dem Terminal ausführen. Öffnen Sie Ihr Terminal und navigieren Sie zum Verzeichnis, in dem sich die `test_reader_flexibility.py`-Datei befindet. Führen Sie dann den folgenden Befehl aus:

```bash
python test_reader_flexibility.py
```

Die Ausgabe sollte in etwa so aussehen:

```
First item from open file: {'name': 'AA', 'shares': 100, 'price': 32.2}

First item from gzipped file: Stock('AA', 100, 32.2)

First item using backward compatible function: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Diese Ausgabe bestätigt, dass unsere Funktionen jetzt mit verschiedenen Arten von Eingabequellen arbeiten, während die Rückwärtskompatibilität gewährleistet bleibt. Die refaktorierten Funktionen können Daten verarbeiten von:

- Normalen Dateien, die mit `open()` geöffnet werden
- Komprimierten Dateien, die mit `gzip.open()` geöffnet werden
- Jedem anderen iterierbaren Objekt, das Textzeilen erzeugt

Dies macht unseren Code viel flexibler und einfacher in verschiedenen Szenarien zu verwenden.
