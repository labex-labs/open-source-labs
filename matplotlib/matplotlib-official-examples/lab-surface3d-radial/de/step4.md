# Zeichnen der Oberfläche

In diesem Schritt werden wir die Oberfläche mit der `plot_surface()`-Funktion von Matplotlib zeichnen. Wir werden die Farbpalette `YlGnBu_r` verwenden, um die Farbe der Oberfläche festzulegen.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
```
