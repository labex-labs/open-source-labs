# Listenelemente entfernen

## Problem

Schreiben Sie eine Funktion `take(itr, n=1)`, die eine Liste `itr` und eine Ganzzahl `n` als Argumente nimmt und eine neue Liste zurückgibt, aus der die ersten `n` Elemente entfernt wurden. Wenn `n` größer als die Länge der Liste ist, geben Sie die ursprüngliche Liste zurück.

## Beispiel

```python
take([1, 2, 3], 1) # [2, 3]
take([1, 2, 3], 2) # [3]
take([1, 2, 3], 3) # []
take([1, 2, 3], 4) # []
```
