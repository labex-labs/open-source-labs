# Liste auffächern

## Problem

Schreiben Sie eine Funktion namens `spread(arg)`, die eine Liste als Argument nimmt und eine neue Liste zurückgibt, die alle Elemente der ursprünglichen Liste enthält, aufgefächert. Wenn ein Element der ursprünglichen Liste selbst eine Liste ist, sollten seine Elemente einzeln zur neuen Liste hinzugefügt werden. Die Funktion sollte die ursprüngliche Liste nicht verändern.

Um die Funktion zu implementieren, sollten Sie über die Elemente der ursprünglichen Liste iterieren und den Spread-Operator verwenden, um die Elemente zur neuen Liste hinzuzufügen. Wenn ein Element eine Liste ist, sollten Sie die `extend()`-Methode verwenden, um seine Elemente zur neuen Liste hinzuzufügen. Wenn ein Element keine Liste ist, sollten Sie die `append()`-Methode verwenden, um es zur neuen Liste hinzuzufügen.

## Beispiel

```python
spread([1, 2, 3, [4, 5, 6], [7], 8, 9]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
