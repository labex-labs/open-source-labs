# Erstellen einer Figur und Achsen

Wir erstellen ein Figurobjekt mit `plt.figure()` und fügen ein Achsenobjekt hinzu, indem wir `fig1.add_axes()` verwenden. Wir legen auch die Größe und Position der Achse mit `[0.1, 0.1, 0.8, 0.8]` fest.

```python
fig1 = plt.figure()
ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
```
