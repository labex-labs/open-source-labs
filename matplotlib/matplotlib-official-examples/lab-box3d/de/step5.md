# Kanten plotten

Plotten Sie die Kanten mit der `plot`-Methode. Wir werden drei Linien entlang der X- und Y-Koordinaten und eine Linie entlang der X- und Z-Koordinaten plotten.

```python
# Plot edges
edges_kw = dict(color='0.4', linewidth=1, zorder=1e3)
ax.plot([xmax, xmax], [ymin, ymax], 0, **edges_kw)
ax.plot([xmin, xmax], [ymin, ymin], 0, **edges_kw)
ax.plot([xmax, xmax], [ymin, ymin], [zmin, zmax], **edges_kw)
```
