# Liste in Blöcke unterteilen

## Problem

Schreiben Sie eine Funktion `chunk(lst, size)`, die eine Liste `lst` und eine positive ganze Zahl `size` als Argumente nimmt und eine Liste von kleineren Listen zurückgibt, von denen jede eine maximale Größe von `size` hat. Wenn die Länge von `lst` nicht ohne Rest durch `size` teilbar ist, sollte die letzte Liste in der zurückgegebenen Liste die verbleibenden Elemente enthalten.

## Beispiel

```python
chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]
chunk([1, 2, 3, 4, 5], 3) # [[1, 2, 3], [4, 5]]
chunk([1, 2, 3, 4, 5], 1) # [[1], [2], [3], [4], [5]]
```
