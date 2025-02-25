# Testen, ob jedes Listelement wahrheitswertig ist

## Problem

Schreiben Sie eine Funktion namens `every(lst, fn = lambda x: x)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte `True` zurückgeben, wenn `fn` für jedes Element in der Liste `True` zurückgibt, und `False` sonst. Wenn keine Funktion angegeben wird, sollte die Funktion standardmäßig die Identitätsfunktion (`lambda x: x`) verwenden.

Um dieses Problem zu lösen, müssen Sie die `all()`-Funktion in Kombination mit `map()` und der bereitgestellten Funktion `fn` verwenden, um zu überprüfen, ob `fn` für alle Elemente in der Liste `True` zurückgibt.

## Beispiel

```python
every([4, 2, 3], lambda x: x > 1) # True
every([1, 2, 3]) # True
every([0, 1, 2]) # False
```
