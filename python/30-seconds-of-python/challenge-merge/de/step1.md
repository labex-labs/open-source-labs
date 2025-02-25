# Listen zusammenführen

## Problem

Schreiben Sie eine Funktion namens `merge(*args, fill_value=None)`, die zwei oder mehr Listen als Argumente nimmt und eine Liste von Listen zurückgibt. Die Funktion sollte Elemente aus jeder der Eingabelisten basierend auf ihrer Position kombinieren. Wenn eine Liste kürzer ist als die längste Liste, sollte die Funktion `fill_value` für die verbleibenden Elemente verwenden. Wenn `fill_value` nicht angegeben ist, sollte sie standardmäßig auf `None` gesetzt werden.

Ihre Aufgabe ist es, die Funktion `merge()` zu implementieren.

## Beispiel

```python
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```
