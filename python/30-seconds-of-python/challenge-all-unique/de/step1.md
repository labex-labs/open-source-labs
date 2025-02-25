# Funktion zum Überprüfen auf Duplikate in einer Liste

## Problemstellung

Schreiben Sie eine Python-Funktion namens `has_duplicates(lst)`, die eine Liste als Argument nimmt und `True` zurückgibt, wenn die Liste doppelte Elemente enthält, andernfalls `False`.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Konvertieren Sie die Liste in einen Satz, um Duplikate zu entfernen.
2. Vergleichen Sie die Länge des Satzes mit der Länge der ursprünglichen Liste.
3. Wenn die Längen gleich sind, hat die Liste keine Duplikate, andernfalls hat sie Duplikate.

## Beispiel

```python
has_duplicates([1, 2, 3, 4, 5]) # False
has_duplicates([1, 2, 3, 4, 5, 5]) # True
has_duplicates(['apple', 'banana', 'orange', 'banana']) # True
has_duplicates([]) # False
```
