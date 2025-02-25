# Listenunterschied

## Problem

Schreiben Sie eine Python-Funktion namens `list_difference(a, b)`, die zwei Listen als Argumente nimmt und den Unterschied zwischen ihnen zurückgibt. Die Funktion sollte doppelte Werte nicht ausschließen. Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Erstellen Sie einen Satz aus der zweiten Liste `b`.
2. Verwenden Sie eine Listenkomprehension auf der ersten Liste `a`, um nur die Werte zu behalten, die nicht im zuvor erstellten Satz `_b` enthalten sind.
3. Geben Sie die resultierende Liste zurück.

## Beispiel

```python
list_difference([1, 2, 3], [1, 2, 4]) # [3]
```
