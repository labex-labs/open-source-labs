# Zeichnen der Fläche

Schließlich zeichnen wir die Fläche mit der Funktion `plot_trisurf()`. Die Dreiecke im Parametersraum bestimmen, welche `x`, `y`, `z`-Punkte durch eine Kante verbunden sind.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_zlim(-1, 1)
```
