# Listen zusammenführen

Schreiben Sie eine Funktion namens `merge(*args, fill_value=None)`, die zwei oder mehr Listen als Argumente nimmt und eine Liste von Listen zurückgibt. Die Funktion sollte Elemente aus jeder der Eingabelisten anhand ihrer Positionen kombinieren. Wenn eine Liste kürzer als die längste Liste ist, sollte die Funktion `fill_value` für die verbleibenden Elemente verwenden. Wenn `fill_value` nicht angegeben ist, sollte der Standardwert `None` sein.

Ihre Aufgabe ist es, die `merge()`-Funktion zu implementieren.

```python
def merge(*args, fill_value = None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result
```

```python
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```
