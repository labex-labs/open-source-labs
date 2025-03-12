# Verständnis des Kontexts

In früheren Übungen haben Sie möglicherweise Code gesehen, der CSV-Dateien liest und die Daten in verschiedenen Datenstrukturen speichert. Das Ziel dieses Codes besteht darin, rohe Textdaten aus einer CSV-Datei zu nehmen und sie in nützlichere Python-Objekte wie Dictionaries oder Klasseninstanzen umzuwandeln. Diese Umwandlung ist essentiell, da sie es uns ermöglicht, mit den Daten in unseren Python-Programmen auf eine strukturierte und sinnvolle Weise zu arbeiten.

Das typische Muster zum Lesen von CSV-Dateien folgt oft einer bestimmten Struktur. Hier ist ein Beispiel für eine Funktion, die eine CSV-Datei liest und jede Zeile in ein Dictionary umwandelt:

```python
import csv

def read_csv_as_dicts(filename, types):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records
```

Lassen Sie uns analysieren, wie diese Funktion funktioniert. Zunächst importiert sie das `csv`-Modul, das Funktionen zum Arbeiten mit CSV-Dateien in Python bereitstellt. Die Funktion nimmt zwei Parameter entgegen: `filename`, der der Name der zu lesenden CSV-Datei ist, und `types`, eine Liste von Funktionen, die zur Umwandlung der Daten in jeder Spalte in den entsprechenden Datentyp verwendet werden.

Innerhalb der Funktion wird eine leere Liste namens `records` initialisiert, um die Dictionaries zu speichern, die jede Zeile der CSV-Datei repräsentieren. Anschließend wird die Datei mit der `with`-Anweisung geöffnet, die sicherstellt, dass die Datei nach der Ausführung des Codeblocks ordnungsgemäß geschlossen wird. Die `csv.reader`-Funktion wird verwendet, um einen Iterator zu erstellen, der jede Zeile der CSV-Datei liest. Die erste Zeile wird als Kopfzeile angenommen und mit der `next`-Funktion abgerufen.

Als nächstes iteriert die Funktion über die verbleibenden Zeilen in der CSV-Datei. Für jede Zeile wird ein Dictionary mit einer Dictionary-Comprehension erstellt. Die Schlüssel des Dictionaries sind die Spaltenüberschriften, und die Werte sind das Ergebnis der Anwendung der entsprechenden Typkonvertierungsfunktion aus der `types`-Liste auf den Wert in der Zeile. Schließlich wird das Dictionary der `records`-Liste hinzugefügt, und die Funktion gibt die Liste der Dictionaries zurück.

Nun schauen wir uns eine ähnliche Funktion an, die Daten aus einer CSV-Datei in Klasseninstanzen liest:

```python
def read_csv_as_instances(filename, cls):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

Diese Funktion ähnelt der vorherigen, erstellt jedoch anstelle von Dictionaries Instanzen einer Klasse. Die Funktion nimmt zwei Parameter entgegen: `filename`, der der Name der zu lesenden CSV-Datei ist, und `cls`, die Klasse, deren Instanzen erstellt werden sollen.

Innerhalb der Funktion folgt sie einer ähnlichen Struktur wie die vorherige Funktion. Sie initialisiert eine leere Liste namens `records`, um die Klasseninstanzen zu speichern. Anschließend wird die Datei geöffnet, die Kopfzeilen gelesen und über die verbleibenden Zeilen iteriert. Für jede Zeile wird die `from_row`-Methode der Klasse `cls` aufgerufen, um eine Instanz der Klasse mit den Daten aus der Zeile zu erstellen. Die Instanz wird dann der `records`-Liste hinzugefügt, und die Funktion gibt die Liste der Instanzen zurück.

In diesem Lab werden wir diese Funktionen refaktorisieren, um sie flexibler und robuster zu machen. Wir werden auch Python's Typ-Hinweis-System (type hinting system) untersuchen, das es uns ermöglicht, die erwarteten Typen der Parameter und Rückgabewerte unserer Funktionen anzugeben. Dies kann unseren Code lesbarer und leichter verständlich machen, insbesondere für andere Entwickler, die möglicherweise mit unserem Code arbeiten.

Lassen Sie uns beginnen, indem wir eine `reader.py`-Datei erstellen und diese Anfangsfunktionen hinzufügen. Stellen Sie sicher, dass Sie diese Funktionen testen, um sicherzustellen, dass sie ordnungsgemäß funktionieren, bevor Sie mit den nächsten Schritten fortfahren.
