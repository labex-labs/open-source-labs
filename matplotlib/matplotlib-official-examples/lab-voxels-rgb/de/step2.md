# Definition der Koordinaten und Farben

Als nächstes müssen wir die Koordinaten und Farben für den Plot definieren. In diesem Beispiel verwenden wir die Funktion `np.indices`, um ein 17x17x17-Gitter von Werten für die RGB-Farben zu erstellen.

```python
r, g, b = np.indices((17, 17, 17)) / 16.0
```

Wir definieren auch eine Funktion `midpoints`, um die Mittelpunkte zwischen den Werten im Gitter zu finden. Dies wird später verwendet, um die Kugel zu erstellen.

```python
def midpoints(x):
    sl = ()
    for _ in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
