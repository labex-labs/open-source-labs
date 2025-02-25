# Das längste Element

## Problemstellung

Schreiben Sie eine Funktion `longest_item(*args)`, die beliebig viele iterierbare Objekte oder Objekte mit einer Länge-Eigenschaft annimmt und das längste zurückgibt. Die Funktion sollte:

- `max()` mit `len()` als `key` verwenden, um das Element mit der größten Länge zurückzugeben.
- Wenn mehrere Elemente die gleiche Länge haben, wird das erste zurückgegeben.

## Beispiel

```python
longest_item('this', 'is', 'a', 'testcase') # 'testcase'
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar') # 'foobar'
```
