# Liste anhand einer Funktion aufteilen

Schreiben Sie eine Funktion `bifurcate_by(lst, fn)`, die eine Liste `lst` und eine Filterfunktion `fn` als Argumente nimmt. Die Funktion sollte die Liste in zwei Gruppen aufteilen, basierend auf dem Ergebnis der Filterfunktion. Wenn die Filterfunktion für ein Element einen wahren Wert zurückgibt, sollte es der ersten Gruppe hinzugefügt werden. Andernfalls sollte es der zweiten Gruppe hinzugefügt werden.

Ihre Funktion sollte eine Liste von zwei Listen zurückgeben, wobei die erste Liste alle Elemente enthält, für die die Filterfunktion einen wahren Wert zurückgegeben hat, und die zweite Liste alle Elemente enthält, für die die Filterfunktion einen falschen Wert zurückgegeben hat.

Verwenden Sie eine Listenkomprehension, um Elemente den Gruppen hinzuzufügen, basierend auf dem Wert, den `fn` für jedes Element zurückgibt.

```python
def bifurcate_by(lst, fn):
  return [
    [x for x in lst if fn(x)],
    [x for x in lst if not fn(x)]
  ]
```

```python
bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```
