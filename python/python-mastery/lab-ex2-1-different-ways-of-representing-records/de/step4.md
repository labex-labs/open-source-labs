# Speicherverbrauch anderer Datenstrukturen

Python bietet viele verschiedene Optionen für die Darstellung von Datenstrukturen. Beispielsweise:

```python
# Ein Tupel
row = (route, date, daytype, rides)

# Ein Wörterbuch
row = {
    'route': route,
    'date': date,
    'daytype': daytype,
    'rides': rides,
}

# Eine Klasse
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# Ein benanntes Tupel
from collections import namedtuple
Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

# Eine Klasse mit __slots__
class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
```

Ihre Aufgabe lautet wie folgt: Erstellen Sie verschiedene Versionen der Funktion `read_rides()`, die jede dieser Datenstrukturen verwenden, um eine einzelne Datenzeile darzustellen. Dann ermitteln Sie den resultierenden Speicherverbrauch jeder Option. Finden Sie heraus, welche Methode die effizienteste Speicherung bietet, wenn Sie mit einer großen Menge an Daten gleichzeitig arbeiten.
