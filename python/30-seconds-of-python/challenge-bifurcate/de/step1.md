# Liste aufteilen

## Problem

Schreiben Sie eine Funktion `bifurcate(lst, filter)`, die eine Liste `lst` und einen Filter `filter` als Eingabe nimmt und eine Liste von zwei Listen zurückgibt. Die erste Liste sollte die Elemente von `lst` enthalten, die den Filter überstehen, und die zweite Liste sollte die Elemente enthalten, die es nicht tun.

Um diese Funktion zu implementieren, können Sie eine Listenkomprehension und die `zip()`-Funktion verwenden. Die `zip()`-Funktion nimmt zwei oder mehr Listen als Eingabe und gibt eine Liste von Tupeln zurück, wobei jedes Tupel die entsprechenden Elemente aus jeder Liste enthält. Beispielsweise gibt `zip([1, 2, 3], [4, 5, 6])` `[(1, 4), (2, 5), (3, 6)]` zurück.

Sie können diese Funktion verwenden, um gleichzeitig über `lst` und `filter` zu iterieren und die Elemente der entsprechenden Liste hinzuzufügen, je nachdem, ob sie den Filter überstehen oder nicht.

## Beispiel

```python
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# Ausgabe: [['beep', 'boop', 'bar'], ['foo']]
```

Im obigen Beispiel ist der Filter `[True, True, False, True]`. Die ersten beiden Elemente von `lst` überstehen den Filter, also werden sie zur ersten Liste hinzugefügt. Das dritte Element übersteht den Filter nicht, also wird es zur zweiten Liste hinzugefügt. Das vierte Element übersteht den Filter, also wird es zur ersten Liste hinzugefügt.
