# 辺をプロットする

`plot` メソッドを使って辺をプロットします。X と Y 座標に沿って 3 本の線を、X と Z 座標に沿って 1 本の線をプロットします。

```python
# Plot edges
edges_kw = dict(color='0.4', linewidth=1, zorder=1e3)
ax.plot([xmax, xmax], [ymin, ymax], 0, **edges_kw)
ax.plot([xmin, xmax], [ymin, ymin], 0, **edges_kw)
ax.plot([xmax, xmax], [ymin, ymin], [zmin, zmax], **edges_kw)
```
