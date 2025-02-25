# Prüfen, ob ein Schlüssel in einem Wörterbuch existiert

## Problemstellung

Schreiben Sie eine Funktion `key_in_dict(d, key)`, die ein Wörterbuch `d` und einen Schlüssel `key` als Argumente übernimmt und `True` zurückgibt, wenn der Schlüssel im Wörterbuch existiert, andernfalls `False`.

## Beispiel

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
key_in_dict(d, 'three') # True
key_in_dict(d,'six') # False
```
