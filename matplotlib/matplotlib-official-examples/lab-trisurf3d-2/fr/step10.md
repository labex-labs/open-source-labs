# Tracer la surface

Enfin, nous traçons la surface à l'aide de la fonction `plot_trisurf()`.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)
```
