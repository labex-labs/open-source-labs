# Arbeiten mit strukturierten Daten mithilfe von Tupeln

Bisher haben wir uns mit der Speicherung von Roh-Text-Daten beschäftigt. Bei der Datenanalyse müssen wir die Daten jedoch in der Regel in organisiertere und strukturierte Formate transformieren. Dies erleichtert es, verschiedene Operationen auszuführen und Erkenntnisse aus den Daten zu gewinnen. In diesem Schritt lernen wir, wie man Daten mithilfe des `csv`-Moduls als Liste von Tupeln liest. Tupel sind eine einfache und nützliche Datenstruktur in Python, die mehrere Werte aufnehmen kann.

## Erstellen einer Lesefunktion mit Tupeln

Erstellen wir eine neue Datei mit dem Namen `readrides.py` im Verzeichnis `/home/labex/project`. Diese Datei enthält den Code, um die Daten aus einer CSV-Datei zu lesen und als Liste von Tupeln zu speichern.

```python
# readrides.py
import csv
import tracemalloc

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    tracemalloc.start()

    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')

    current, peak = tracemalloc.get_traced_memory()
    print(f'Number of records: {len(rows)}')
    print(f'First record: {rows[0]}')
    print(f'Second record: {rows[1]}')
    print(f'Memory Use: Current {current/1024/1024:.2f} MB, Peak {peak/1024/1024:.2f} MB')
```

Dieses Skript definiert eine Funktion namens `read_rides_as_tuples`. Hier ist, was sie Schritt für Schritt macht:

1. Sie öffnet die CSV-Datei, die durch den `filename`-Parameter angegeben wird. Dadurch können wir auf die Daten in der Datei zugreifen.
2. Sie verwendet das `csv`-Modul, um jede Zeile der Datei zu analysieren. Die `csv.reader`-Funktion hilft uns, die Zeilen in einzelne Werte aufzuteilen.
3. Sie extrahiert die vier Felder (Linie, Datum, Tagestyp und Anzahl der Fahrten) aus jeder Zeile. Diese Felder sind für unsere Datenanalyse wichtig.
4. Sie konvertiert das Feld 'rides' in eine Ganzzahl. Dies ist notwendig, da die Daten in der CSV-Datei zunächst im Zeichenkettenformat vorliegen und wir einen numerischen Wert für Berechnungen benötigen.
5. Sie erstellt ein Tupel mit diesen vier Werten. Tupel sind unveränderlich, was bedeutet, dass ihre Werte nach der Erstellung nicht geändert werden können.
6. Sie fügt das Tupel einer Liste namens `records` hinzu. Diese Liste enthält alle Datensätze aus der CSV-Datei.

Jetzt führen wir das Skript aus. Öffnen Sie Ihr Terminal und geben Sie den folgenden Befehl ein:

```bash
python3 /home/labex/project/readrides.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Number of records: 577563
First record: ('3', '01/01/2001', 'U', 7354)
Second record: ('4', '01/01/2001', 'U', 9288)
Memory Use: Current 89.12 MB, Peak 89.15 MB
```

Beachten Sie, dass der Speicherverbrauch im Vergleich zu unseren vorherigen Beispielen gestiegen ist. Es gibt einige Gründe dafür:

1. Wir speichern die Daten jetzt in einem strukturierten Format (Tupeln). Strukturierte Daten erfordern in der Regel mehr Speicher, da sie eine definierte Organisation haben.
2. Jeder Wert im Tupel ist ein separates Python-Objekt. Python-Objekte haben einen gewissen Overhead, der zum erhöhten Speicherverbrauch beiträgt.
3. Wir haben eine zusätzliche Listenstruktur, die alle diese Tupel enthält. Listen nehmen auch Speicherplatz in Anspruch, um ihre Elemente zu speichern.

Der Vorteil dieses Ansatzes ist, dass unsere Daten jetzt richtig strukturiert und für die Analyse bereit sind. Wir können leicht auf bestimmte Felder jedes Datensatzes über den Index zugreifen. Beispielsweise:

```python
# Example of accessing tuple elements (add this to readrides.py file to try it)
first_record = rows[0]
route = first_record[0]
date = first_record[1]
daytype = first_record[2]
rides = first_record[3]
print(f"Route: {route}, Date: {date}, Day type: {daytype}, Rides: {rides}")
```

Allerdings ist der Zugriff auf Daten über numerische Indizes nicht immer intuitiv. Es kann schwierig sein, sich zu merken, welcher Index welchem Feld entspricht, insbesondere wenn es viele Felder gibt. Im nächsten Schritt werden wir andere Datenstrukturen untersuchen, die unseren Code lesbarer und wartbarer machen können.
