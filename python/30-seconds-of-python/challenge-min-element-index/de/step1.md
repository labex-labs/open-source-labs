# Index des kleinsten Elements

## Problemstellung

Schreibe eine Funktion `min_element_index(arr)`, die eine Liste von ganzen Zahlen `arr` als Argument nimmt und den Index des Elements mit dem kleinsten Wert in der Liste zurückgibt.

Um dieses Problem zu lösen, kannst du die `min()`-Funktion verwenden, um den kleinsten Wert in der Liste zu erhalten, und dann die `list.index()`-Methode verwenden, um seinen Index zurückzugeben.

## Beispiel

```python
min_element_index([3, 5, 2, 6, 10, 7, 9]) # 2
```

In diesem Beispiel ist der kleinste Wert in der Liste `[3, 5, 2, 6, 10, 7, 9]` der Wert `2`, der sich an Index `2` befindet.
