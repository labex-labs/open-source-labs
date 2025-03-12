# Erstellen einer Hilfsfunktion für die CSV-Verarbeitung

Nachdem wir nun verstehen, wie Python's First-Class-Objekte uns bei der Datenkonvertierung helfen können, werden wir eine wiederverwendbare Hilfsfunktion erstellen. Diese Funktion wird CSV-Daten lesen und sie in eine Liste von Wörterbüchern umwandeln. Dies ist eine sehr nützliche Operation, da CSV-Dateien häufig zur Speicherung tabellarischer Daten verwendet werden, und die Umwandlung in eine Liste von Wörterbüchern erleichtert die Arbeit mit den Daten in Python.

## Erstellen der CSV-Leser-Hilfsfunktion

Zunächst öffnen Sie die WebIDE. Sobald sie geöffnet ist, navigieren Sie zum Projektverzeichnis und erstellen Sie eine neue Datei mit dem Namen `reader.py`. In dieser Datei werden wir eine Funktion definieren, die CSV-Daten liest und Typkonvertierungen anwendet. Typkonvertierungen sind wichtig, da die Daten in einer CSV-Datei normalerweise als Zeichenketten gelesen werden, aber wir möglicherweise andere Datentypen wie Ganzzahlen oder Fließkommazahlen für die weitere Verarbeitung benötigen.

Fügen Sie den folgenden Code in `reader.py` ein:

```python
import csv

def read_csv_as_dicts(filename, types):
    """
    Read a CSV file into a list of dictionaries, converting each field according
    to the types provided.

    Parameters:
    filename (str): Name of the CSV file to read
    types (list): List of type conversion functions for each column

    Returns:
    list: List of dictionaries representing the CSV data
    """
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get the column headers

        for row in rows:
            # Apply type conversions to each value in the row
            converted_row = [func(val) for func, val in zip(types, row)]

            # Create a dictionary mapping headers to converted values
            record = dict(zip(headers, converted_row))
            records.append(record)

    return records
```

Diese Funktion öffnet zunächst die angegebene CSV-Datei. Dann liest sie die Kopfzeilen der CSV-Datei, die die Namen der Spalten sind. Danach geht sie jede Zeile in der Datei durch. Für jeden Wert in der Zeile wendet sie die entsprechende Typkonvertierungsfunktion aus der `types`-Liste an. Schließlich erstellt sie ein Wörterbuch, in dem die Schlüssel die Spaltenüberschriften und die Werte die konvertierten Daten sind, und fügt dieses Wörterbuch der `records`-Liste hinzu. Sobald alle Zeilen verarbeitet sind, gibt sie die `records`-Liste zurück.

## Testen der Hilfsfunktion

Lassen Sie uns unsere Hilfsfunktion testen. Zunächst öffnen Sie ein Terminal und starten Sie einen Python-Interpreter, indem Sie Folgendes eingeben:

```bash
python3
```

Jetzt, da wir im Python-Interpreter sind, können wir unsere Funktion verwenden, um die Portfolio-Daten zu lesen. Die Portfolio-Daten sind eine CSV-Datei, die Informationen über Aktien enthält, wie den Namen der Aktie, die Anzahl der Anteile und den Preis.

```python
import reader
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
for record in portfolio[:3]:  # Show the first 3 records
    print(record)
```

Wenn Sie diesen Code ausführen, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
{'name': 'IBM', 'shares': 50, 'price': 91.1}
{'name': 'CAT', 'shares': 150, 'price': 83.44}
```

Diese Ausgabe zeigt die ersten drei Datensätze aus den Portfolio-Daten, wobei die Datentypen korrekt konvertiert wurden.

Lassen Sie uns auch unsere Funktion mit den CTA-Bus-Daten testen. Die CTA-Bus-Daten sind eine andere CSV-Datei, die Informationen über Buslinien, Daten, Tagestypen und die Anzahl der Fahrten enthält.

```python
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])
print(f"Total rows: {len(rows)}")
print("First row:", rows[0])
```

Die Ausgabe sollte in etwa so aussehen:

```
Total rows: 577563
First row: {'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
```

Dies zeigt, dass unsere Funktion verschiedene CSV-Dateien verarbeiten und die entsprechenden Typkonvertierungen anwenden kann.

Um den Python-Interpreter zu beenden, geben Sie ein:

```python
exit()
```

Sie haben nun eine wiederverwendbare Hilfsfunktion erstellt, die jede CSV-Datei lesen und die entsprechenden Typkonvertierungen anwenden kann. Dies zeigt die Stärke von Python's First-Class-Objekten und wie sie zur Erstellung flexiblen, wiederverwendbaren Codes genutzt werden können.
