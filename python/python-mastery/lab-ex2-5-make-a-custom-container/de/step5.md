# Verbesserung des benutzerdefinierten Containers für Slicing

Unser benutzerdefinierter Container eignet sich hervorragend für den Zugriff auf einzelne Datensätze. Allerdings gibt es ein Problem, wenn es um Slicing geht. Wenn Sie versuchen, einen Teil unseres Containers auszuschneiden (slicen), ist das Ergebnis nicht das, was Sie normalerweise erwarten würden.

Lassen Sie uns verstehen, warum dies passiert. In Python ist Slicing eine gängige Operation, um einen Teil einer Sequenz zu extrahieren. Aber für unseren benutzerdefinierten Container weiß Python nicht, wie es ein neues `RideData` - Objekt nur mit den ausgeschnittenen Daten erstellen soll. Stattdessen erstellt es eine Liste, die die Ergebnisse des Aufrufs von `__getitem__` für jeden Index im Schnitt enthält.

1. Testen wir das Slicing in der Python - Shell:

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # This will likely be a list, not a RideData object
print(r)  # This might look like a list of numbers, not dictionaries
```

In diesem Code importieren wir zunächst das Modul `readrides`. Dann lesen wir die Daten aus der Datei `ctabus.csv` in eine Variable `rows`. Wenn wir versuchen, einen Schnitt der ersten 10 Datensätze zu nehmen und den Typ des Ergebnisses überprüfen, stellen wir fest, dass es eine Liste anstelle eines `RideData` - Objekts ist. Das Drucken des Ergebnisses könnte etwas Unerwartetes anzeigen, wie eine Liste von Zahlen anstelle von Wörterbüchern.

2. Modifizieren wir unsere `RideData` - Klasse, um Slicing richtig zu behandeln. Öffnen Sie `readrides.py` und aktualisieren Sie die Methode `__getitem__`:

```python
def __getitem__(self, index):
    if isinstance(index, slice):
        # Handle slice
        result = RideData()
        result.routes = self.routes[index]
        result.dates = self.dates[index]
        result.daytypes = self.daytypes[index]
        result.numrides = self.numrides[index]
        return result
    else:
        # Handle single index
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}
```

In dieser aktualisierten Methode `__getitem__` überprüfen wir zunächst, ob der `index` ein Schnitt ist. Wenn dies der Fall ist, erstellen wir ein neues `RideData` - Objekt namens `result`. Dann füllen wir dieses neue Objekt mit Schnitten der ursprünglichen Datenspalten (`routes`, `dates`, `daytypes` und `numrides`). Dies stellt sicher, dass wir beim Slicing unseres benutzerdefinierten Containers ein weiteres `RideData` - Objekt anstelle einer Liste erhalten. Wenn der `index` kein Schnitt ist (d. h., es ist ein einzelner Index), geben wir ein Wörterbuch zurück, das den relevanten Datensatz enthält.

3. Testen wir unsere verbesserte Slicing - Fähigkeit:

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # Should now be readrides.RideData
len(r)   # Should be 10
r[0]     # Should be the same as rows[0]
r[1]     # Should be the same as rows[1]
```

Nachdem wir die Methode `__getitem__` aktualisiert haben, können wir das Slicing erneut testen. Wenn wir einen Schnitt der ersten 10 Datensätze nehmen, sollte der Typ des Ergebnisses jetzt `readrides.RideData` sein. Die Länge des Schnitts sollte 10 sein, und der Zugriff auf einzelne Elemente im Schnitt sollte die gleichen Ergebnisse liefern wie der Zugriff auf die entsprechenden Elemente im ursprünglichen Container.

4. Sie können auch mit verschiedenen Schnittmustern testen:

```python
# Get every other record from the first 20
r2 = rows[0:20:2]
len(r2)  # Should be 10

# Get the last 10 records
r3 = rows[-10:]
len(r3)  # Should be 10
```

Hier testen wir verschiedene Schnittmuster. Der erste Schnitt `rows[0:20:2]` holt jedes zweite Element aus den ersten 20 Datensätzen, und die Länge des resultierenden Schnitts sollte 10 sein. Der zweite Schnitt `rows[-10:]` holt die letzten 10 Datensätze, und seine Länge sollte ebenfalls 10 sein.

Durch die korrekte Implementierung des Slicings verhält sich unser benutzerdefinierter Container jetzt noch mehr wie eine Standard - Python - Liste, während er gleichzeitig die Speichereffizienz der spaltenorientierten Speicherung beibehält.

Dieser Ansatz, benutzerdefinierte Containerklassen zu erstellen, die integrierte Python - Container imitieren, aber eine andere interne Darstellung haben, ist eine leistungsstarke Technik, um den Speicherverbrauch zu optimieren, ohne die Schnittstelle zu ändern, die Ihr Code den Benutzern bietet.
