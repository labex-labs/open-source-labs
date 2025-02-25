# Das letzte übereinstimmende Element finden

## Problemstellung

Schreiben Sie eine Funktion `find_last(lst, fn)`, die eine Liste `lst` und eine Testfunktion `fn` als Argumente übernimmt. Die Funktion sollte den Wert des letzten Elements in `lst` zurückgeben, für das `fn` `True` zurückgibt. Wenn kein Element der Testfunktion entspricht, sollte die Funktion `None` zurückgeben.

Um dieses Problem zu lösen, sollten Sie Listenverständnis und `next()` verwenden, um die Liste in umgekehrter Reihenfolge durchzugehen und das letzte Element zurückzugeben, das der Testfunktion entspricht.

## Beispiel

```python
find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
find_last([2, 4, 6, 8], lambda n: n % 2 == 1) # None
```

Im ersten Beispiel sollte die Funktion `3` zurückgeben, da es die letzte ungerade Zahl in der Liste ist. Im zweiten Beispiel sollte die Funktion `None` zurückgeben, da es keine ungeraden Zahlen in der Liste gibt.
