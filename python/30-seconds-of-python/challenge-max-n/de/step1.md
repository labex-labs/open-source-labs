# Herausforderung: Die n größten Elemente

## Problemstellung

Schreiben Sie eine Funktion `max_n(lst, n = 1)`, die eine Liste `lst` und einen optionalen Integer `n` als Argumente nimmt und eine Liste der `n` größten Elemente aus der bereitgestellten Liste zurückgibt. Wenn `n` nicht angegeben wird, sollte die Funktion eine Liste zurückgeben, die das maximale Element der Liste enthält. Wenn `n` größer als oder gleich der Länge der Liste ist, sollte die Funktion die ursprüngliche Liste in absteigender Reihenfolge zurückgeben.

Ihre Aufgabe ist es, die Funktion `max_n()` zu implementieren.

## Beispiel

```python
max_n([1, 2, 3]) # [3]
max_n([1, 2, 3], 2) # [3, 2]
max_n([1, 2, 3, 4, 5], 3) # [5, 4, 3]
max_n([1, 2, 3, 4, 5], 6) # [5, 4, 3, 2, 1]
```
