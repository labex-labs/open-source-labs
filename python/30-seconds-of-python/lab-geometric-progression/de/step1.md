# Geometrische Reihe

Schreiben Sie eine Funktion namens `geometric_progression`, die drei Parameter annimmt:

- `end`: eine Ganzzahl, die das Ende des Bereichs (inklusiv) repräsentiert
- `start`: eine optionale Ganzzahl, die den Anfang des Bereichs (inklusiv) repräsentiert, mit einem Standardwert von `1`
- `step`: eine optionale Ganzzahl, die das gemeinsame Verhältnis zwischen zwei aufeinanderfolgenden Gliedern repräsentiert, mit einem Standardwert von `2`

Die Funktion sollte eine Liste zurückgeben, die die Zahlen im angegebenen Bereich enthält, wobei das Verhältnis zwischen zwei aufeinanderfolgenden Gliedern `step` beträgt. Die Liste sollte mit `start` beginnen und mit `end` enden.

Wenn `step` gleich `1` ist, sollte die Funktion einen Fehler zurückgeben.

Sie sollten `range()`, `math.log()` und `math.floor()` und eine List Comprehension verwenden, um eine Liste der passenden Länge zu erstellen und den Schritt für jedes Element anzuwenden.

```python
from math import floor, log

def geometric_progression(end, start=1, step=2):
  return [start * step ** i for i in range(floor(log(end / start)
          / log(step)) + 1)]
```

```python
geometric_progression(256) # [1, 2, 4, 8, 16, 32, 64, 128, 256]
geometric_progression(256, 3) # [3, 6, 12, 24, 48, 96, 192]
geometric_progression(256, 1, 4) # [1, 4, 16, 64, 256]
```
