# Schlüssel des kleinsten Werts

## Problemstellung

Schreiben Sie eine Funktion `key_of_min(d)`, die ein Wörterbuch `d` als Argument erhält und den Schlüssel des kleinsten Werts im Wörterbuch zurückgibt.

Um dieses Problem zu lösen, können Sie die integrierte `min()`-Funktion mit dem Parameter `key` auf `dict.get()` setzen. Dies wird den Schlüssel des kleinsten Werts im Wörterbuch zurückgeben.

## Beispiel

```python
key_of_min({'a':4, 'b':0, 'c':13}) # 'b'
```

In diesem Beispiel wird das Wörterbuch `{'a':4, 'b':0, 'c':13}` als Argument an die `key_of_min()`-Funktion übergeben. Die Funktion gibt den Schlüssel `'b'` zurück, der dem kleinsten Wert im Wörterbuch entspricht.
