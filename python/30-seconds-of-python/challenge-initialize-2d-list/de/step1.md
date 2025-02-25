# 2D-Liste initialisieren

## Problemstellung

Schreiben Sie eine Funktion `initialize_2d_list(w, h, val=None)`, die eine 2D-Liste mit gegebener Breite, Höhe und Wert initialisiert. Die Funktion sollte eine Liste von `h` Zeilen zurückgeben, wobei jede Zeile eine Liste mit der Länge `w` ist, die mit `val` initialisiert ist. Wenn `val` nicht angegeben ist, sollte der Standardwert `None` sein.

## Beispiel

```python
initialize_2d_list(2, 2, 0) # [[0, 0], [0, 0]]
initialize_2d_list(3, 3, "x") # [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
initialize_2d_list(2, 3) # [[None, None], [None, None], [None, None]]
```
