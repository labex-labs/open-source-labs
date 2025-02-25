# Tracer les bords

Tracez les bords en utilisant la méthode `plot`. Nous tracerons trois lignes le long des coordonnées X et Y, et une ligne le long des coordonnées X et Z.

```python
# Tracer les bords
edges_kw = dict(color='0.4', linewidth=1, zorder=1e3)
ax.plot([xmax, xmax], [ymin, ymax], 0, **edges_kw)
ax.plot([xmin, xmax], [ymin, ymin], 0, **edges_kw)
ax.plot([xmax, xmax], [ymin, ymin], [zmin, zmax], **edges_kw)
```
