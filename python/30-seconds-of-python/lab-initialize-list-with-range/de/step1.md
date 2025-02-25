# Liste mit Bereich initialisieren

Schreiben Sie eine Funktion `initialize_list_with_range(end, start=0, step=1)`, die eine Liste initialisiert, die die Zahlen im angegebenen Bereich enthält, wobei `start` und `end` inklusive sind und deren gemeinsamer Unterschied `step` ist.

Die Funktion sollte eine Liste der passenden Länge zurückgeben, die mit den gewünschten Werten im angegebenen Bereich gefüllt ist.

### Eingabe

- `end` (ganzzahlig) - Das Ende des Bereichs (inklusiv).
- `start` (ganzzahlig, optional) - Der Anfang des Bereichs (inklusiv). Standardwert ist 0.
- `step` (ganzzahlig, optional) - Der gemeinsame Unterschied zwischen jeder Zahl im Bereich. Standardwert ist 1.

### Ausgabe

- Eine Liste, die die Zahlen im angegebenen Bereich enthält.

```python
def initialize_list_with_range(end, start = 0, step = 1):
  return list(range(start, end + 1, step))
```

```python
initialize_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialize_list_with_range(7, 3) # [3, 4, 5, 6, 7]
initialize_list_with_range(9, 0, 2) # [0, 2, 4, 6, 8]
```
