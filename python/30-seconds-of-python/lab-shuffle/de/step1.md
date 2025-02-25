# Liste mischen

Schreiben Sie eine Funktion `shuffle(lst)`, die eine Liste als Eingabe nimmt und eine neue Liste zurückgibt, die die gleichen Elemente in zufälliger Reihenfolge enthält. Ihre Funktion sollte den Fisher-Yates-Algorithmus verwenden, um die Elemente in der Liste zu mischen.

Der Fisher-Yates-Algorithmus funktioniert wie folgt:

1. Beginne mit dem letzten Element in der Liste.
2. Generiere einen zufälligen Index zwischen 0 und dem aktuellen Index.
3. Tausche das Element am aktuellen Index mit dem Element am zufälligen Index.
4. Gehe zum nächsten Element in der Liste und wiederhole die Schritte 2-3, bis alle Elemente gemischt sind.

Ihre Funktion sollte die ursprüngliche Liste nicht verändern. Stattdessen sollte sie eine neue Liste mit den gemischten Elementen erstellen.

Sie können davon ausgehen, dass die Eingabeliste mindestens ein Element enthalten wird.

```python
from copy import deepcopy
from random import randint

def shuffle(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst
```

```python
foo = [1, 2, 3]
shuffle(foo) # [2, 3, 1], foo = [1, 2, 3]
```
