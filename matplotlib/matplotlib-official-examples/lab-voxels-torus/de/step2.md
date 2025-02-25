# Mittelpunkte-Funktion definieren

Als nächstes definieren wir eine `midpoints`-Funktion, um die Mittelpunkte eines Arrays von Koordinaten zu berechnen. Diese Funktion wird später verwendet, um die Mittelpunkte von `r`, `theta` und `z` zu berechnen.

```python
def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
