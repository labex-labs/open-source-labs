# Nicht eindeutige Liste-Werte filtern

## Problem

Schreiben Sie eine Python-Funktion namens `filter_non_unique(lst)`, die eine Liste als Argument nimmt und eine neue Liste mit nur den eindeutigen Werten zurückgibt. Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie die `collections.Counter`-Methode, um die Anzahl jedes Werts in der Liste zu erhalten.
2. Verwenden Sie eine Listenkomprehension, um eine Liste zu erstellen, die nur die eindeutigen Werte enthält.

## Beispiel

```python
filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]
filter_non_unique(['apple', 'banana', 'apple', 'orange', 'pear', 'banana']) # ['orange', 'pear']
```
