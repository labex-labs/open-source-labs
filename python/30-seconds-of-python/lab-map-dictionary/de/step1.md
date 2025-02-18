# Liste in ein Wörterbuch abbilden

Schreiben Sie eine Python-Funktion namens `map_dictionary(itr, fn)`, die zwei Parameter akzeptiert:

- `itr`: Eine Liste von Werten
- `fn`: Eine Funktion, die einen Wert als Eingabe nimmt und einen Wert als Ausgabe zurückgibt

Die Funktion sollte ein Wörterbuch (dictionary) zurückgeben, bei dem die Schlüssel-Wert-Paare aus dem ursprünglichen Wert als Schlüssel und dem Ergebnis der Funktion als Wert bestehen.

Um dieses Problem zu lösen, folgen Sie diesen Schritten:

1. Verwenden Sie `map()`, um `fn` auf jeden Wert der Liste anzuwenden.
2. Verwenden Sie `zip()`, um die ursprünglichen Werte mit den von `fn` erzeugten Werten zu verknüpfen.
3. Verwenden Sie `dict()`, um ein passendes Wörterbuch zurückzugeben.

```python
def map_dictionary(itr, fn):
  return dict(zip(itr, map(fn, itr)))
```

```python
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```
