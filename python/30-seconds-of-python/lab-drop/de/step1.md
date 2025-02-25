# Entfernen von Listelementen von der Linken

Schreiben Sie eine Funktion `drop(a, n=1)`, die eine Liste `a` und einen optionalen Integer `n` als Argumente nimmt und eine neue Liste zurückgibt, aus der die ersten `n` Elemente der ursprünglichen Liste entfernt wurden. Wenn `n` nicht angegeben wird, sollte die Funktion nur das erste Element der Liste entfernen.

```python
def drop(a, n = 1):
  return a[n:]
```

```python
drop([1, 2, 3]) # [2, 3]
drop([1, 2, 3], 2) # [3]
drop([1, 2, 3], 42) # []
```
