# Exploration des Datensatzes

Beginnen wir unsere Reise, indem wir uns den Datensatz genauer ansehen, mit dem wir arbeiten werden. Die Datei `ctabus.csv` ist eine CSV-Datei (Comma-Separated Values, deutsch: durch Kommas getrennte Werte). CSV-Dateien sind eine gängige Methode zur Speicherung tabellarischer Daten, bei der jede Zeile eine Zeile in der Tabelle darstellt und die Werte innerhalb einer Zeile durch Kommas getrennt sind. Diese spezielle Datei enthält tägliche Fahrgastzahldaten für das Busssystem der Chicago Transit Authority (CTA) und deckt den Zeitraum vom 1. Januar 2001 bis zum 31. August 2013 ab.

Um die Struktur dieser Datei zu verstehen, werfen wir zunächst einen Blick hinein. Wir verwenden Python, um die Datei zu lesen und einige Zeilen auszugeben. Öffnen Sie ein Terminal und führen Sie den folgenden Python-Code aus:

```python
f = open('/home/labex/project/ctabus.csv')
print(next(f))  # Read the header line
print(next(f))  # Read the first data line
print(next(f))  # Read the second data line
f.close()
```

In diesem Code öffnen wir zunächst die Datei mit der `open`-Funktion und weisen sie der Variable `f` zu. Die `next`-Funktion wird verwendet, um die nächste Zeile aus der Datei zu lesen. Wir verwenden sie dreimal: das erste Mal, um die Kopfzeile zu lesen, die normalerweise die Namen der Spalten im Datensatz enthält. Das zweite und dritte Mal lesen we jeweils die erste und zweite Datenzeile. Schließlich schließen wir die Datei mit der `close`-Methode, um Systemressourcen freizugeben.

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
route,date,daytype,rides

3,01/01/2001,U,7354

4,01/01/2001,U,9288
```

Diese Ausgabe zeigt, dass die Datei 4 Spalten mit Daten enthält. Lassen Sie uns analysieren, was jede Spalte darstellt:

1. `route`: Dies ist der Name oder die Nummer der Buslinie. Es ist die erste Spalte (Spalte 0) im Datensatz.
2. `date`: Dies ist ein Datum als Zeichenkette im Format MM/TT/JJJJ. Dies ist die zweite Spalte (Spalte 1).
3. `daytype`: Dies ist ein Code für den Tagestyp und die dritte Spalte (Spalte 2).
   - U = Sonntag/Ferientag
   - A = Samstag
   - W = Werktag
4. `rides`: Diese Spalte enthält die Gesamtzahl der Fahrgäste als Ganzzahl. Es ist die vierte Spalte (Spalte 3).

Die Spalte `rides` zeigt uns, wie viele Personen an einem bestimmten Tag eine Buslinie benutzt haben. Beispielsweise können wir aus der obigen Ausgabe sehen, dass am 1. Januar 2001 7.354 Personen die Buslinie Nummer 3 benutzt haben.

Jetzt wollen wir herausfinden, wie viele Zeilen die Datei enthält. Die Anzahl der Zeilen gibt uns eine Vorstellung von der Größe unseres Datensatzes. Führen Sie den folgenden Python-Code aus:

```python
with open('/home/labex/project/ctabus.csv') as f:
    line_count = sum(1 for line in f)
    print(f"Total lines in the file: {line_count}")
```

In diesem Code verwenden wir die `with`-Anweisung, um die Datei zu öffnen. Der Vorteil der `with`-Anweisung ist, dass sie automatisch dafür sorgt, dass die Datei geschlossen wird, wenn wir fertig sind. Dann verwenden wir einen Generatorausdruck `(1 for line in f)`, um eine Sequenz von Einsen zu erstellen, eine für jede Zeile in der Datei. Die `sum`-Funktion summiert all diese Einsen auf und gibt uns die Gesamtzahl der Zeilen in der Datei. Schließlich geben wir das Ergebnis aus.

Die Ausgabe sollte ungefähr 577.564 Zeilen betragen, was bedeutet, dass wir es mit einem beträchtlichen Datensatz zu tun haben. Dieser große Datensatz bietet uns genügend Daten, um zu analysieren und Erkenntnisse zu gewinnen.
