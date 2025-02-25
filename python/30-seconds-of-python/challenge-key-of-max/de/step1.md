# Schlüssel des maximalen Werts

## Problem

Schreiben Sie eine Funktion `key_of_max(d)`, die ein Dictionary `d` als Argument nimmt und den Schlüssel des maximalen Werts im Dictionary zurückgibt. Wenn es mehrere Schlüssel mit dem gleichen maximalen Wert gibt, geben Sie irgendeinen von ihnen zurück.

Um dieses Problem zu lösen, können Sie die `max()`-Funktion mit dem `key`-Parameter auf `dict.get()` setzen. Dies wird den Schlüssel des maximalen Werts im Dictionary zurückgeben.

## Beispiel

```python
key_of_max({'a':4, 'b':0, 'c':13}) # 'c'
```
