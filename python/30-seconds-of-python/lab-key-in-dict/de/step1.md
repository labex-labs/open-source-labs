# Prüfen, ob ein Schlüssel in einem Dictionary existiert

Schreiben Sie eine Funktion `key_in_dict(d, key)`, die ein Dictionary `d` und einen Schlüssel `key` als Argumente übernimmt und `True` zurückgibt, wenn der Schlüssel im Dictionary existiert, andernfalls `False`.

```python
def key_in_dict(d, key):
  return (key in d)
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
key_in_dict(d, 'three') # True
```
