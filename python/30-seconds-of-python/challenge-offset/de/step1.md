# Elemente einer Liste um Offset verschieben

## Problem

Schreiben Sie eine Funktion `offset(lst, offset)`, die eine Liste `lst` und einen Integer `offset` als Argumente übernimmt und eine neue Liste zurückgibt, in der die angegebenen Anzahl von Elementen ans Ende der Liste verschoben sind. Wenn der `offset` positiv ist, werden die ersten `offset` Elemente ans Ende der Liste verschoben. Wenn der `offset` negativ ist, werden die letzten `offset` Elemente ans Anfang der Liste verschoben.

## Beispiel

```python
offset([1, 2, 3, 4, 5], 2) # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2) # [4, 5, 1, 2, 3]
```
