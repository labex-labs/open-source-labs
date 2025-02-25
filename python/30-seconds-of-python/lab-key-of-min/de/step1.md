# Schlüssel des kleinsten Werts

Schreiben Sie eine Funktion `key_of_min(d)`, die ein Dictionary `d` als Argument nimmt und den Schlüssel des kleinsten Werts im Dictionary zurückgibt.

Um dieses Problem zu lösen, können Sie die integrierte `min()`-Funktion mit dem Parameter `key` auf `dict.get()` setzen. Dies wird den Schlüssel des kleinsten Werts im Dictionary zurückgeben.

```python
def key_of_min(d):
  return min(d, key = d.get)
```

```python
key_of_min({'a':4, 'b':0, 'c':13}) # b
```
