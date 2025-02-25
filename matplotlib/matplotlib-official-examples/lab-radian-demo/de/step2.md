# Daten erstellen

Erstellen Sie einen Array von Werten zwischen 0 und 15 in Schritten von 0,01 und konvertieren Sie sie in Radiant mit der radians-Funktion aus dem basic_units-Paket.

```python
from basic_units import radians
x = [val*radians for val in np.arange(0, 15, 0.01)]
```
