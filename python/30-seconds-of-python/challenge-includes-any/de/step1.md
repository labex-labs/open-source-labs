# Überprüfen, ob ein Wert in einer Liste in einer anderen Liste enthalten ist

## Problemstellung

Schreiben Sie eine Funktion `includes_any(lst, values)`, die zwei Listen als Argumente annimmt. Die Funktion sollte überprüfen, ob irgendein Element in `values` in `lst` enthalten ist. Wenn ein Wert gefunden wird, sollte die Funktion `True` zurückgeben, andernfalls sollte sie `False` zurückgeben.

Um dieses Problem zu lösen, können Sie eine `for-Schleife` verwenden, um durch jeden Wert in `values` zu iterieren. Anschließend können Sie den `in-Operator` verwenden, um zu überprüfen, ob der Wert in `lst` enthalten ist. Wenn ein Wert gefunden wird, geben Sie `True` zurück. Wenn kein Wert gefunden wird, geben Sie `False` zurück.

## Beispiel

```python
includes_any([1, 2, 3, 4], [2, 9]) # True
includes_any([1, 2, 3, 4], [8, 9]) # False
```
