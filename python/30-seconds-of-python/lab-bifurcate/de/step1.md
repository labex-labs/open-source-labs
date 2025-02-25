# Liste aufteilen

Schreiben Sie eine Funktion `bifurcate(lst, filter)`, die eine Liste `lst` und einen Filter `filter` als Eingabe nimmt und eine Liste von zwei Listen zurückgibt. Die erste Liste sollte die Elemente von `lst` enthalten, die den Filter bestehen, und die zweite Liste sollte die Elemente enthalten, die ihn nicht bestehen.

Um diese Funktion zu implementieren, können Sie eine List Comprehension und die `zip()`-Funktion verwenden. Die `zip()`-Funktion nimmt zwei oder mehr Listen als Eingabe und gibt eine Liste von Tupeln zurück, wobei jedes Tupel die entsprechenden Elemente aus jeder Liste enthält. Beispielsweise gibt `zip([1, 2, 3], [4, 5, 6])` `[(1, 4), (2, 5), (3, 6)]` zurück.

Sie können diese Funktion verwenden, um gleichzeitig über `lst` und `filter` zu iterieren und die Elemente der entsprechenden Liste hinzuzufügen, je nachdem, ob sie den Filter bestehen oder nicht.

```python
def bifurcate(lst, filter):
  return [
    [x for x, flag in zip(lst, filter) if flag],
    [x for x, flag in zip(lst, filter) if not flag]
  ]
```

```python
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```
