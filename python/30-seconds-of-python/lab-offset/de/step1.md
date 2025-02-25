# Elemente einer Liste um einen Offset verschieben

Schreiben Sie eine Funktion `offset(lst, offset)`, die eine Liste `lst` und einen Integer `offset` als Argumente übernimmt und eine neue Liste zurückgibt, in der die angegebenen Anzahl von Elementen ans Ende der Liste verschoben sind. Wenn der `offset` positiv ist, bewegen Sie die ersten `offset` Elemente ans Ende der Liste. Wenn der `offset` negativ ist, bewegen Sie die letzten `offset` Elemente ans Anfang der Liste.

```python
def offset(lst, offset):
  return lst[offset:] + lst[:offset]
```

```python
offset([1, 2, 3, 4, 5], 2) # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2) # [4, 5, 1, 2, 3]
```
