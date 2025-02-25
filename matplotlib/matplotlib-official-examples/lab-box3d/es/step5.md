# Grafica los bordes

Grafica los bordes utilizando el método `plot`. Grafica tres líneas a lo largo de las coordenadas X e Y, y una línea a lo largo de las coordenadas X y Z.

```python
# Grafica los bordes
edges_kw = dict(color='0.4', linewidth=1, zorder=1e3)
ax.plot([xmax, xmax], [ymin, ymax], 0, **edges_kw)
ax.plot([xmin, xmax], [ymin, ymin], 0, **edges_kw)
ax.plot([xmax, xmax], [ymin, ymin], [zmin, zmax], **edges_kw)
```
