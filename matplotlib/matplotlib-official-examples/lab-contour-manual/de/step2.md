# Definieren der Konturlinien und Polygone

Der nächste Schritt besteht darin, die Konturlinien und Polygone zu definieren. In diesem Beispiel haben wir Linien und gefüllte Konturen zwischen zwei Ebenen.

```python
# Die Konturlinien für jede Ebene sind eine Liste/Tupel von Polygonen.
lines0 = [[[0, 0], [0, 4]]]
lines1 = [[[2, 0], [1, 2], [1, 3]]]
lines2 = [[[3, 0], [3, 2]], [[3, 3], [3, 4]]]  # Beachten Sie zwei Linien.

# Gefüllte Konturen zwischen zwei Ebenen sind ebenfalls eine Liste/Tupel von Polygonen.
# Die Punkte können im Uhrzeigersinn oder gegen den Uhrzeigersinn geordnet sein.
filled01 = [[[0, 0], [0, 4], [1, 3], [1, 2], [2, 0]]]
filled12 = [[[2, 0], [3, 0], [3, 2], [1, 3], [1, 2]],   # Beachten Sie zwei Polygone.
            [[1, 4], [3, 4], [3, 3]]]
```
