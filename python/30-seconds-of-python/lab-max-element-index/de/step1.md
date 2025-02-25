# Index des größten Elements

Schreiben Sie eine Funktion `max_element_index(arr)`, die eine Liste `arr` als Argument nimmt und den Index des Elements mit dem maximalen Wert zurückgibt. Wenn es mehrere Elemente mit dem maximalen Wert gibt, geben Sie den Index des ersten Vorkommens zurück.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie die integrierte `max()`-Funktion, um den maximalen Wert in der Liste zu finden.
2. Verwenden Sie die integrierte `list.index()`-Funktion, um den Index des ersten Vorkommens des maximalen Werts in der Liste zu finden.
3. Geben Sie den Index zurück.

```python
def max_element_index(arr):
  return arr.index(max(arr))
```

```python
max_element_index([5, 8, 9, 7, 10, 3, 0]) # 4
```
