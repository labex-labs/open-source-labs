# Grundlegende Iteration und Sequenzentpackung

In diesem Schritt werden wir die grundlegende Iteration mit `for`-Schleifen und die Sequenzentpackung in Python untersuchen. Iteration ist ein grundlegendes Konzept in der Programmierung, das es Ihnen ermöglicht, jedes Element in einer Sequenz nacheinander zu durchlaufen. Die Sequenzentpackung hingegen ermöglicht es Ihnen, die einzelnen Elemente einer Sequenz bequem Variablen zuzuweisen.

## Laden von Daten aus einer CSV-Datei

Beginnen wir damit, einige Daten aus einer CSV-Datei zu laden. CSV (Comma-Separated Values, deutsch: durch Kommas getrennte Werte) ist ein gängiges Dateiformat zur Speicherung tabellarischer Daten. Um zu beginnen, müssen wir im WebIDE ein Terminal öffnen und den Python-Interpreter starten. Dadurch können wir Python-Code interaktiv ausführen.

```bash
cd ~/project
python3
```

Jetzt, da wir im Python-Interpreter sind, können wir den folgenden Python-Code ausführen, um Daten aus der `portfolio.csv`-Datei zu lesen. Zunächst importieren wir das `csv`-Modul, das Funktionen für die Arbeit mit CSV-Dateien bereitstellt. Dann öffnen wir die Datei und erstellen ein `csv.reader`-Objekt, um die Daten zu lesen. Wir verwenden die `next`-Funktion, um die Spaltenüberschriften zu erhalten, und wandeln die verbleibenden Daten in eine Liste um. Schließlich verwenden wir die `pprint`-Funktion aus dem `pprint`-Modul, um die Zeilen in einem lesbareren Format auszugeben.

```python
import csv

f = open('portfolio.csv')
f_csv = csv.reader(f)
headers = next(f_csv)    # Get the column headers
rows = list(f_csv)       # Convert the remaining data to a list
from pprint import pprint
pprint(rows)             # Pretty print the rows
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
[['AA', '100', '32.20'],
 ['IBM', '50', '91.10'],
 ['CAT', '150', '83.44'],
 ['MSFT', '200', '51.23'],
 ['GE', '95', '40.37'],
 ['MSFT', '50', '65.10'],
 ['IBM', '100', '70.44']]
```

## Grundlegende Iteration mit `for`-Schleifen

Die `for`-Anweisung in Python wird verwendet, um über jede Datensequenz wie eine Liste, ein Tupel oder einen String zu iterieren. In unserem Fall verwenden wir sie, um über die Zeilen der Daten zu iterieren, die wir aus der CSV-Datei geladen haben.

```python
for row in rows:
    print(row)
```

Dieser Code durchläuft jede Zeile in der `rows`-Liste und gibt sie aus. Sie werden jede Datenzeile aus unserer CSV-Datei nacheinander sehen.

```
['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
```

## Sequenzentpackung in Schleifen

Python ermöglicht es Ihnen, Sequenzen direkt in einer `for`-Schleife zu entpacken. Dies ist sehr nützlich, wenn Sie die Struktur jedes Elements in der Sequenz kennen. In unserem Fall enthält jede Zeile in der `rows`-Liste drei Elemente: einen Namen, die Anzahl der Aktien und den Preis. Wir können diese Elemente direkt in der `for`-Schleife entpacken.

```python
for name, shares, price in rows:
    print(name, shares, price)
```

Dieser Code entpackt jede Zeile in die Variablen `name`, `shares` und `price` und gibt sie dann aus. Sie werden die Daten in einem lesbareren Format sehen.

```
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
```

Wenn Sie einige Werte nicht benötigen, können Sie `_` als Platzhalter verwenden, um anzuzeigen, dass Sie diese Werte nicht interessieren. Beispielsweise können Sie, wenn Sie nur den Namen und den Preis ausgeben möchten, den folgenden Code verwenden:

```python
for name, _, price in rows:
    print(name, price)
```

Dieser Code ignoriert das zweite Element in jeder Zeile und gibt nur den Namen und den Preis aus.

```
AA 32.20
IBM 91.10
CAT 83.44
MSFT 51.23
GE 40.37
MSFT 65.10
IBM 70.44
```

## Erweiterte Entpackung mit dem `*`-Operator

Für eine fortgeschrittenere Entpackung können Sie den `*`-Operator als Wildcard verwenden. Dies ermöglicht es Ihnen, mehrere Elemente in einer Liste zu sammeln. Lassen Sie uns unsere Daten anhand des Namens mit dieser Technik gruppieren.

```python
from collections import defaultdict

byname = defaultdict(list)
for name, *data in rows:
    byname[name].append(data)

# Print the data for IBM
print(byname['IBM'])

# Iterate through IBM's data
for shares, price in byname['IBM']:
    print(shares, price)
```

In diesem Code importieren wir zunächst die `defaultdict`-Klasse aus dem `collections`-Modul. Ein `defaultdict` ist ein Wörterbuch, das automatisch einen neuen Wert (in diesem Fall eine leere Liste) erstellt, wenn der Schlüssel nicht existiert. Dann verwenden wir den `*`-Operator, um alle Elemente außer dem ersten in einer Liste namens `data` zu sammeln. Wir speichern diese Liste im `byname`-Wörterbuch, gruppiert nach dem Namen. Schließlich geben wir die Daten für IBM aus und durchlaufen sie, um die Anzahl der Aktien und den Preis auszugeben.

Ausgabe:

```
[['50', '91.10'], ['100', '70.44']]
50 91.10
100 00.44
```

In diesem Beispiel sammelt `*data` alle Elemente außer dem ersten in einer Liste, die wir dann in einem nach Namen gruppierten Wörterbuch speichern. Dies ist eine leistungsstarke Technik zur Verarbeitung von Daten mit Sequenzen variabler Länge.
