# Den letzten übereinstimmenden Wert finden

Schreiben Sie eine Funktion `find_last(lst, fn)`, die eine Liste `lst` und eine Prüfungsfunktion `fn` als Argumente nimmt. Die Funktion sollte den Wert des letzten Elements in `lst` zurückgeben, für das `fn` `True` zurückgibt. Wenn kein Element der Prüfungsfunktion entspricht, sollte die Funktion `None` zurückgeben.

Um dieses Problem zu lösen, sollten Sie eine Listenkomprehension und `next()` verwenden, um die Liste in umgekehrter Reihenfolge durchzugehen und das letzte Element zurückzugeben, das der Prüfungsfunktion entspricht.

```python
def find_last(lst, fn):
  return next(x for x in lst[::-1] if fn(x))
```

```python
find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
```
