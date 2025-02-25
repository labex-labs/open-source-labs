# Liste in Dictionary abbilden

## Problem

Schreiben Sie eine Python-Funktion namens `map_dictionary(itr, fn)`, die zwei Parameter akzeptiert:

- `itr`: Eine Liste von Werten
- `fn`: Eine Funktion, die einen Wert als Eingabe nimmt und einen Wert als Ausgabe zurückgibt

Die Funktion sollte ein Dictionary zurückgeben, wobei die Schlüssel-Wert-Paare aus dem ursprünglichen Wert als Schlüssel und dem Ergebnis der Funktion als Wert bestehen.

Um dieses Problem zu lösen, führen Sie die folgenden Schritte aus:

1. Verwenden Sie `map()`, um `fn` auf jedes Element der Liste anzuwenden.
2. Verwenden Sie `zip()`, um die ursprünglichen Werte mit den von `fn` erzeugten Werten zu verknüpfen.
3. Verwenden Sie `dict()`, um ein passendes Dictionary zurückzugeben.

## Beispiel

```python
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```

In diesem Beispiel nimmt die `map_dictionary()`-Funktion eine Liste `[1, 2, 3]` und eine Lambda-Funktion `lambda x: x * x` als Eingabe. Die Lambda-Funktion quadriert den Eingabewert. Die Funktion gibt ein Dictionary `{ 1: 1, 2: 4, 3: 9 }` zurück, wobei die Schlüssel die ursprünglichen Werte der Liste sind und die Werte die quadrierten Werte.
