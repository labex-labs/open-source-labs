# Entschachtele eine Liste

Schreiben Sie eine Python-Funktion namens `flatten(lst)`, die eine Liste von Listen als Argument nimmt und eine entschachtelte Liste zurückgibt. Die Funktion sollte die Liste nur einmal entschachteln, was bedeutet, dass alle geschachtelten Listen innerhalb der ursprünglichen Liste entschachtelt werden sollten, aber alle geschachtelten Listen innerhalb dieser geschachtelten Listen sollten unverändert bleiben.

Um dieses Problem zu lösen, können Sie eine Listenkomprehension verwenden, um jeden Wert aus den Unterlisten in der Reihenfolge zu extrahieren.

```python
def flatten(lst):
  return [x for y in lst for x in y]
```

```python
flatten([[1, 2, 3, 4], [5, 6, 7, 8]]) # [1, 2, 3, 4, 5, 6, 7, 8]
```
