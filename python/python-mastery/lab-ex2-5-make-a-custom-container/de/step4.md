# Erstellen einer benutzerdefinierten Containerklasse

Bei der Datenverarbeitung ist der spaltenorientierte Ansatz hervorragend geeignet, um Speicher zu sparen. Allerdings kann es Probleme geben, wenn Ihr bestehender Code erwartet, dass die Daten in Form einer Liste von Wörterbüchern (Dictionaries) vorliegen. Um dieses Problem zu lösen, erstellen wir eine benutzerdefinierte Containerklasse. Diese Klasse wird eine zeilenorientierte Schnittstelle bieten, was bedeutet, dass sie für Ihren Code wie eine Liste von Wörterbüchern aussehen und verhalten wird. Intern wird sie jedoch die Daten in spaltenorientierter Form speichern, was uns hilft, Speicher zu sparen.

1. Öffnen Sie zunächst die Datei `readrides.py` im WebIDE - Editor. Wir werden dieser Datei eine neue Klasse hinzufügen. Diese Klasse wird die Grundlage für unseren benutzerdefinierten Container bilden.

```python
# Add this to readrides.py
from collections.abc import Sequence

class RideData(Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

In diesem Code definieren wir eine Klasse namens `RideData`, die von `Sequence` erbt. Die Methode `__init__` initialisiert vier leere Listen, wobei jede Liste eine Spalte der Daten darstellt. Die Methode `__len__` gibt die Länge des Containers zurück, die der Länge der `routes` - Liste entspricht. Die Methode `__getitem__` ermöglicht es uns, einen bestimmten Datensatz anhand des Indexes zuzugreifen und ihn als Wörterbuch zurückzugeben. Die Methode `append` fügt einen neuen Datensatz zum Container hinzu, indem sie die Werte an jede Spaltenliste anhängt.

2. Jetzt benötigen wir eine Funktion, um die Busfahrtdaten in unseren benutzerdefinierten Container einzulesen. Fügen Sie die folgende Funktion zur Datei `readrides.py` hinzu.

```python
# Add this to readrides.py
def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts, but use our custom container
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

Diese Funktion erstellt eine Instanz der Klasse `RideData` und füllt sie mit Daten aus der CSV - Datei. Sie liest jede Zeile aus der Datei, extrahiert die relevanten Informationen, erstellt für jeden Datensatz ein Wörterbuch und fügt es dann dem `RideData` - Container hinzu. Das Wichtigste ist, dass sie die gleiche Schnittstelle wie eine Liste von Wörterbüchern aufrechterhält, aber die Daten intern spaltenweise speichert.

3. Testen wir unseren benutzerdefinierten Container in der Python - Shell. Dies wird uns helfen, zu überprüfen, ob er wie erwartet funktioniert.

```python
import readrides

# Read the data using our custom container
rows = readrides.read_rides_as_dicts('ctabus.csv')

# Check the type of the returned object
type(rows)  # Should be readrides.RideData

# Check the length
len(rows)   # Should be 577563

# Access individual records
rows[0]     # Should return a dictionary for the first record
rows[1]     # Should return a dictionary for the second record
rows[2]     # Should return a dictionary for the third record
```

Unser benutzerdefinierter Container implementiert erfolgreich die `Sequence` - Schnittstelle, was bedeutet, dass er sich wie eine Liste verhält. Sie können die Funktion `len()` verwenden, um die Anzahl der Datensätze im Container zu erhalten, und Sie können die Indizierung verwenden, um einzelne Datensätze zuzugreifen. Jeder Datensatz scheint ein Wörterbuch zu sein, obwohl die Daten intern spaltenweise gespeichert sind. Dies ist großartig, da bestehender Code, der eine Liste von Wörterbüchern erwartet, weiterhin mit unserem benutzerdefinierten Container ohne jegliche Modifikationen funktioniert.

4. Schließlich messen wir den Speicherverbrauch unseres benutzerdefinierten Containers. Dies wird uns zeigen, wie viel Speicher wir im Vergleich zu einer Liste von Wörterbüchern sparen.

```python
import tracemalloc

tracemalloc.start()
rows = readrides.read_rides_as_dicts('ctabus.csv')
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")
tracemalloc.stop()
```

Wenn Sie diesen Code ausführen, sollten Sie feststellen, dass der Speicherverbrauch ähnlich dem des spaltenorientierten Ansatzes ist, der viel geringer ist als der einer Liste von Wörterbüchern. Dies zeigt den Vorteil unseres benutzerdefinierten Containers in Bezug auf die Speichereffizienz.
