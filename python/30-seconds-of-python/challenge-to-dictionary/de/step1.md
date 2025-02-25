# Listen in ein Dictionary umwandeln

## Problemstellung

Schreiben Sie eine Funktion `to_dictionary(keys, values)`, die zwei Listen als Eingabe nimmt und ein Dictionary zurückgibt, wobei die Elemente der ersten Liste als Schlüssel und die Elemente der zweiten Liste als Werte dienen. Die Funktion sollte `zip()` in Kombination mit `dict()` verwenden, um die Werte der beiden Listen zu einem Dictionary zu kombinieren. Die Funktion sollte `None` zurückgeben, wenn die Länge der beiden Listen nicht gleich ist.

## Beispiel

```python
to_dictionary(['a', 'b'], [1, 2]) # { 'a': 1, 'b': 2 }
to_dictionary(['a', 'b', 'c'], [1, 2]) # None
```
