# Erstellen einer höheren Funktion (Higher-Order Function)

In Python ist eine höhere Funktion (Higher-Order Function) eine Funktion, die eine andere Funktion als Argument nehmen kann. Dies ermöglicht eine größere Flexibilität und Code-Wiederverwendung. Jetzt erstellen wir eine höhere Funktion namens `convert_csv()`. Diese Funktion wird die gemeinsamen Operationen bei der Verarbeitung von CSV-Daten übernehmen, während Sie festlegen können, wie jede Zeile der CSV-Datei in einen Datensatz umgewandelt wird.

Öffnen Sie die Datei `reader.py` im WebIDE. Wir werden eine Funktion hinzufügen, die ein iterierbares Objekt mit CSV-Daten, eine Konvertierungsfunktion und optional Spaltenüberschriften (Headers) nimmt. Die Konvertierungsfunktion wird verwendet, um jede Zeile der CSV-Datei in einen Datensatz umzuwandeln.

Hier ist der Code für die `convert_csv()`-Funktion. Kopieren Sie ihn und fügen Sie ihn in Ihre `reader.py`-Datei ein:

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function

    Args:
        lines: An iterable containing CSV data
        conversion_func: A function that takes headers and a row and returns a record
        headers: Column headers (optional). If None, the first row is used as headers

    Returns:
        A list of records as processed by conversion_func
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = conversion_func(headers, row)
        records.append(record)
    return records
```

Lassen Sie uns analysieren, was diese Funktion tut. Zunächst initialisiert sie eine leere Liste namens `records`, um die konvertierten Datensätze zu speichern. Dann verwendet sie die `csv.reader()`-Funktion, um die Zeilen der CSV-Daten zu lesen. Wenn keine Spaltenüberschriften angegeben werden, nimmt sie die erste Zeile als Spaltenüberschriften. Für jede nachfolgende Zeile wendet sie die `conversion_func` an, um die Zeile in einen Datensatz umzuwandeln und fügt diesen der `records`-Liste hinzu. Schließlich gibt sie die Liste der Datensätze zurück.

Jetzt benötigen wir eine einfache Konvertierungsfunktion, um unsere `convert_csv()`-Funktion zu testen. Diese Funktion nimmt die Spaltenüberschriften und eine Zeile und wandelt die Zeile in ein Dictionary um, wobei die Spaltenüberschriften als Schlüssel verwendet werden.

Hier ist der Code für die `make_dict()`-Funktion. Fügen Sie diese Funktion ebenfalls zu Ihrer `reader.py`-Datei hinzu:

```python
def make_dict(headers, row):
    '''
    Convert a row to a dictionary using the provided headers
    '''
    return dict(zip(headers, row))
```

Die `make_dict()`-Funktion verwendet die `zip()`-Funktion, um jede Spaltenüberschrift mit ihrem entsprechenden Wert in der Zeile zu verknüpfen und erstellt dann ein Dictionary aus diesen Paaren.

Lassen Sie uns diese Funktionen testen. Öffnen Sie eine Python-Shell, indem Sie die folgenden Befehle im Terminal ausführen:

```bash
cd ~/project
python3 -i reader.py
```

Die `-i`-Option im `python3`-Befehl startet den Python-Interpreter im interaktiven Modus und importiert die `reader.py`-Datei, sodass wir die Funktionen verwenden können, die wir gerade definiert haben.

In der Python-Shell führen Sie den folgenden Code aus, um unsere Funktionen zu testen:

```python
# Open the CSV file
lines = open('portfolio.csv')

# Convert to a list of dictionaries using our new function
result = convert_csv(lines, make_dict)

# Print the result
print(result)
```

Dieser Code öffnet die `portfolio.csv`-Datei, verwendet die `convert_csv()`-Funktion mit der `make_dict()`-Konvertierungsfunktion, um die CSV-Daten in eine Liste von Dictionaries umzuwandeln, und gibt dann das Ergebnis aus.

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

Diese Ausgabe zeigt, dass unsere höhere Funktion `convert_csv()` korrekt funktioniert. Wir haben erfolgreich eine Funktion erstellt, die eine andere Funktion als Argument nimmt, was es uns ermöglicht, leicht zu ändern, wie die CSV-Daten konvertiert werden.

Um die Python-Shell zu verlassen, können Sie `exit()` eingeben oder Strg+D drücken.
