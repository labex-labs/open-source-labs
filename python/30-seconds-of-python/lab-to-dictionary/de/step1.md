# Listen in ein Dictionary umwandeln

Schreiben Sie eine Funktion `to_dictionary(keys, values)`, die zwei Listen als Eingabe nimmt und ein Dictionary zurückgibt, wobei die Elemente der ersten Liste als Schlüssel und die Elemente der zweiten Liste als Werte dienen. Die Funktion sollte `zip()` in Kombination mit `dict()` verwenden, um die Werte der beiden Listen zu einem Dictionary zu kombinieren. Die Funktion sollte `None` zurückgeben, wenn die Länge der beiden Listen nicht gleich ist.

```python
def to_dictionary(keys, values):
  return dict(zip(keys, values))
```

```python
to_dictionary(['a', 'b'], [1, 2]) # { a: 1, b: 2 }
```
