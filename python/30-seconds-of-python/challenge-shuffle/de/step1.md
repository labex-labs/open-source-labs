# Liste mischen

## Problem

Schreiben Sie eine Funktion `shuffle(lst)`, die eine Liste als Eingabe nimmt und eine neue Liste zurückgibt, in der die gleichen Elemente in zufälliger Reihenfolge stehen. Ihre Funktion sollte den Fisher-Yates-Algorithmus verwenden, um die Elemente in der Liste zu mischen.

Der Fisher-Yates-Algorithmus funktioniert wie folgt:

1. Beginnen Sie mit dem letzten Element in der Liste.
2. Generieren Sie einen zufälligen Index zwischen 0 und dem aktuellen Index.
3. Tauschen Sie das Element an dem aktuellen Index mit dem Element an dem zufälligen Index.
4. Gehen Sie zum nächsten Element in der Liste und wiederholen Sie Schritte 2-3, bis alle Elemente gemischt wurden.

Ihre Funktion sollte die ursprüngliche Liste nicht verändern. Stattdessen sollte sie eine neue Liste mit den gemischten Elementen erstellen.

Sie können davon ausgehen, dass die Eingabeliste mindestens ein Element enthalten wird.

## Beispiel

```python
foo = [1, 2, 3, 4, 5]
shuffled_foo = shuffle(foo)
print(shuffled_foo) # [3, 1, 4, 5, 2]
print(foo) # [1, 2, 3, 4, 5]
```
