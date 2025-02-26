# Eine Liste von Tupeln

In der Praxis könnten Sie die Daten in eine Liste lesen und jede Zeile in eine andere Datenstruktur umwandeln. Hier ist ein Programm `readrides.py`, das die gesamte Datei in eine Liste von Tupeln liest, indem das Modul `csv` verwendet wird:

```python
# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    Liest die Busfahrtdaten als Liste von Tupeln
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Überspringe die Überschriften
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')
    print('Speicherverbrauch: Aktuell %d, Spitze %d' % tracemalloc.get_traced_memory())
```

Führen Sie dieses Programm mit `python3 -i readrides.py` aus und betrachten Sie die resultierenden Inhalte von `rows`. Sie sollten eine Liste von Tupeln wie diese erhalten:

```python
>>> len(rows)
577563
>>> rows[0]
('3', '01/01/2001', 'U', 7354)
>>> rows[1]
('4', '01/01/2001', 'U', 9288)
```

Betrachten Sie den resultierenden Speicherverbrauch. Er sollte erheblich höher sein als in Schritt 2.
