# Erstellen eines benutzerdefinierten Containers - Der große Täuschungsversuch

Das Speichern der Daten in Spalten bietet eine erheblich bessere Arbeitsspeichersparnis, aber die Daten sind jetzt ziemlich schwierig zu verarbeiten. Tatsächlich kann keiner unserer früheren Analysecodes aus Übung 2.2 mit Spalten umgehen. Der Grund, warum alles kaputtgeht, ist, dass Sie die Datenabstraktion, die in früheren Übungen verwendet wurde, nämlich die Annahme, dass die Daten als Liste von Wörterbüchern gespeichert sind, zerstört haben.

Dies kann behoben werden, wenn Sie bereit sind, einen benutzerdefinierten Containerobjekt zu erstellen, das dies "nachmacht". Lassen Sie uns das tun.

Der frühere Analysecode nimmt an, dass die Daten in einer Sequenz von Datensätzen gespeichert sind. Jeder Datensatz wird als Wörterbuch dargestellt. Lassen Sie uns beginnen, eine neue "Sequenz"-Klasse zu erstellen. In dieser Klasse speichern wir die vier Spalten der Daten, die in der `read_rides_as_columns()`-Funktion verwendet wurden.

```python
# readrides.py

from collections.abc import Sequence

...

class RideData(Sequence):
    def __init__(self):
        self.routes = []      # Spalten
        self.dates = []
        self.daytypes = []
        self.numrides = []
```

Versuchen Sie, eine `RideData`-Instanz zu erstellen. Sie werden feststellen, dass es mit einer Fehlermeldung wie dieser fehlschlägt:

```python
>>> records = RideData()
Traceback (most recent call last):
...
TypeError: Can't instantiate abstract class RideData with abstract methods __getitem__, __len__
>>>
```

Lesen Sie die Fehlermeldung sorgfältig. Sie sagt uns, was wir implementieren müssen. Fügen Sie eine `__len__()`- und `__getitem__()`-Methode hinzu. In der `__getitem__()`-Methode werden wir ein Wörterbuch erstellen. Darüber hinaus erstellen wir eine `append()`-Methode, die ein Wörterbuch nimmt und es in 4 separate `append()`-Operationen aufpackt.

```python
# readrides.py
...

class RideData(collections.Sequence):
    def __init__(self):
        # Jeder Wert ist eine Liste mit allen Werten (eine Spalte)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # Alle Listen werden angenommen, die gleiche Länge zu haben
        return len(self.routes)

    def __getitem__(self, index):
        return { 'route': self.routes[index],
                 'date': self.dates[index],
                 'daytype': self.daytypes[index],
                 'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

Wenn Sie dies richtig gemacht haben, sollten Sie dieses Objekt in die zuvor geschriebene `read_rides_as_dicts()`-Funktion einfügen können. Dazu müssen Sie nur eine Zeile des Codes ändern:

```python
# readrides.py
...

def read_rides_as_dicts(filename):
    '''
    Liest die Busfahrtdaten als Liste von Wörterbüchern ein
    '''
    records = RideData()      # <--- ÄNDERN SIE DIES
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Überspringt die Überschriften
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides' : rides
                }
            records.append(record)
    return records
```

Wenn Sie dies richtig gemacht haben, sollte der alte Code genauso funktionieren wie zuvor. Beispielsweise:

```python
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> rows[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> rows[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>> rows[2]
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
>>>
```

Führen Sie Ihren früheren CTA-Code aus Übung 2.2 aus. Er sollte ohne Änderungen funktionieren, aber erheblich weniger Arbeitsspeicher verwenden.
