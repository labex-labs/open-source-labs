# Plotar Bordas

Plote as bordas usando o método `plot`. Vamos plotar três linhas ao longo das coordenadas X e Y, e uma linha ao longo das coordenadas X e Z.

```python
# Plot edges
edges_kw = dict(color='0.4', linewidth=1, zorder=1e3)
ax.plot([xmax, xmax], [ymin, ymax], 0, **edges_kw)
ax.plot([xmin, xmax], [ymin, ymin], 0, **edges_kw)
ax.plot([xmax, xmax], [ymin, ymin], [zmin, zmax], **edges_kw)
```
