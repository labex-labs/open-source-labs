# Kompakte Liste

## Problem

Schreibe eine Funktion `compact(lst)`, die eine Liste als Argument nimmt und eine neue Liste zurückgibt, aus der alle falschen Werte entfernt wurden. Falsche Werte umfassen `False`, `None`, `0` und `""`.

Um dieses Problem zu lösen, kannst du die `filter()`-Funktion verwenden, um falsche Werte aus der Liste zu filtern.

## Beispiel

```python
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```
