# Erkundung des Datensatzes

Beginnen wir unsere Reise mit einem genauen Blick auf den Datensatz, mit dem wir arbeiten werden. Die Datei `ctabus.csv` ist eine CSV-Datei (Comma-Separated Values, Komma-getrennte Werte). CSV-Dateien sind eine gängige Methode zur Speicherung tabellarischer Daten, wobei jede Zeile eine Reihe darstellt und die Werte innerhalb einer Reihe durch Kommas getrennt sind. Diese spezielle Datei enthält tägliche Fahrgastzahlen für das Bussystem der Chicago Transit Authority (CTA) im Zeitraum vom 1. Januar 2001 bis zum 31. August 2013.

Entpacken Sie die Datei und entfernen Sie die Zip-Datei:

```bash
cd /home/labex/project
unzip ctabus.csv.zip
rm ctabus.csv.zip
```

Um die Struktur dieser Datei zu verstehen, werfen wir zunächst einen Blick hinein. Wir werden Python verwenden, um die Datei zu lesen und einige Zeilen auszugeben. Öffnen Sie ein Terminal und führen Sie den folgenden Python-Code aus:

```python
f = open('/home/labex/project/ctabus.csv')
print(next(f))  # Read the header line
print(next(f))  # Read the first data line
print(next(f))  # Read the second data line
f.close()
```

In diesem Code öffnen wir zuerst die Datei mit der Funktion `open` und weisen sie der Variablen `f` zu. Die Funktion `next` wird verwendet, um die nächste Zeile aus der Datei zu lesen. Wir verwenden sie dreimal: das erste Mal, um die Kopfzeile (header line) zu lesen, die normalerweise die Namen der Spalten im Datensatz enthält. Das zweite und dritte Mal lesen wir die erste bzw. zweite Datenzeile. Schließlich schließen wir die Datei mit der Methode `close`, um Systemressourcen freizugeben.

Sie sollten eine ähnliche Ausgabe wie diese sehen:

```
route,date,daytype,rides

3,01/01/2001,U,7354

4,01/01/2001,U,9288
```

Diese Ausgabe zeigt, dass die Datei 4 Datenspalten hat. Lassen Sie uns aufschlüsseln, was jede Spalte darstellt:

1. `route`: Dies ist der Name oder die Nummer der Buslinie (bus route). Es ist die erste Spalte (Spalte 0) im Datensatz.
2. `date`: Dies ist eine Datumszeichenfolge (date string) im Format MM/TT/JJJJ. Dies ist die zweite Spalte (Spalte 1).
3. `daytype`: Dies ist ein Tagestyp-Code (day type code), der die dritte Spalte (Spalte 2) ist.
   - U = Sonntag/Feiertag (Sunday/Holiday)
   - A = Samstag (Saturday)
   - W = Wochentag (Weekday)
4. `rides`: Diese Spalte erfasst die Gesamtzahl der Fahrgäste als ganze Zahl (integer). Es ist die vierte Spalte (Spalte 3).

Die Spalte `rides` gibt an, wie viele Personen an einem bestimmten Tag in eine bestimmte Buslinie eingestiegen sind. Aus der obigen Ausgabe können wir beispielsweise ersehen, dass am 1. Januar 2001 7.354 Personen mit der Buslinie 3 gefahren sind.

Finden wir nun heraus, wie viele Zeilen sich in der Datei befinden. Die Kenntnis der Anzahl der Zeilen gibt uns eine Vorstellung von der Größe unseres Datensatzes. Führen Sie den folgenden Python-Code aus:

```python
with open('/home/labex/project/ctabus.csv') as f:
    line_count = sum(1 for line in f)
    print(f"Total lines in the file: {line_count}")
```

In diesem Code verwenden wir die `with`-Anweisung, um die Datei zu öffnen. Der Vorteil der Verwendung von `with` besteht darin, dass es sich automatisch um das Schließen der Datei kümmert, wenn wir damit fertig sind. Wir verwenden dann einen Generatorausdruck `(1 for line in f)`, um eine Sequenz von Einsen zu erstellen, eine für jede Zeile in der Datei. Die Funktion `sum` addiert alle diese Einsen und ergibt die Gesamtzahl der Zeilen in der Datei. Schließlich geben wir das Ergebnis aus.

Dies sollte ungefähr 577.564 Zeilen ausgeben, was bedeutet, dass wir es mit einem umfangreichen Datensatz zu tun haben. Dieser große Datensatz wird uns viele Daten liefern, die wir analysieren und aus denen wir Erkenntnisse gewinnen können.
