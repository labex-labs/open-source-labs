# Elemente aus der linken Seite einer Liste entfernen

## Problemstellung

Schreiben Sie eine Funktion `drop(a, n=1)`, die eine Liste `a` und einen optionalen Integer `n` als Argumente übernimmt und eine neue Liste zurückgibt, aus der die ersten `n` Elemente der ursprünglichen Liste entfernt wurden. Wenn `n` nicht angegeben wird, soll die Funktion nur das erste Element der Liste entfernen.

## Beispiel

```python
drop([1, 2, 3]) # [2, 3]
drop([1, 2, 3], 2) # [3]
drop([1, 2, 3], 42) # []
```
