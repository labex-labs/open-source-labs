# Tracer la surface

Enfin, nous traçons la surface à l'aide de la fonction `plot_trisurf()`. Les triangles dans l'espace de paramètres déterminent quels points `x`, `y`, `z` sont connectés par un bord.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_zlim(-1, 1)
```
