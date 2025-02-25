# Liste anhand einer Funktion aufteilen

## Problemstellung

Schreiben Sie eine Funktion `bifurcate_by(lst, fn)`, die eine Liste `lst` und eine Filterfunktion `fn` als Argumente übernimmt. Die Funktion sollte die Liste in zwei Gruppen aufteilen, basierend auf dem Ergebnis der Filterfunktion. Wenn die Filterfunktion für ein Element einen wahren Wert zurückgibt, sollte es der ersten Gruppe hinzugefügt werden. Andernfalls sollte es der zweiten Gruppe hinzugefügt werden.

Ihre Funktion sollte eine Liste von zwei Listen zurückgeben, wobei die erste Liste alle Elemente enthält, für die die Filterfunktion einen wahren Wert zurückgegeben hat, und die zweite Liste alle Elemente enthält, für die die Filterfunktion einen falschen Wert zurückgegeben hat.

Verwenden Sie eine Listenkomprehension, um Elemente den Gruppen hinzuzufügen, basierend auf dem Wert, den `fn` für jedes Element zurückgibt.

## Beispiel

```python
bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```

Im obigen Beispiel wird die Funktion mit einer Liste von Strings und einer Filterfunktion aufgerufen, die überprüft, ob das erste Zeichen jedes Strings 'b' ist. Die Funktion gibt eine Liste von zwei Listen zurück, wobei die erste Liste alle Strings enthält, die mit 'b' beginnen, und die zweite Liste alle anderen Strings enthält.
