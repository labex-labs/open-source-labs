# Entfernen von Listelementen von der rechten Seite

## Problemstellung

Schreiben Sie eine Funktion `drop_right(a, n = 1)`, die eine Liste `a` und eine optionale Ganzzahl `n` entgegennimmt und eine neue Liste zurückgibt, aus der `n` Elemente von der rechten Seite der Liste `a` entfernt wurden. Wenn `n` nicht angegeben wird, sollte die Funktion nur das letzte Element aus der Liste entfernen.

## Beispiel

```python
drop_right([1, 2, 3]) # [1, 2]
drop_right([1, 2, 3], 2) # [1]
drop_right([1, 2, 3], 42) # []
```
