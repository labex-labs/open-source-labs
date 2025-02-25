# Zeichnen der 3D-Oberfläche

In diesem Schritt zeichnen wir die 3D-Oberfläche mit den Testdaten und passen das Aussehen des Plots an.

```python
# Zeichnen der 3D-Oberfläche
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)

# Passen das Aussehen des Plots an
ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100), xlabel='X', ylabel='Y', zlabel='Z')
```
