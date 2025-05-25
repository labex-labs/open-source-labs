# 가장자리 플롯

`plot` 메서드를 사용하여 가장자리를 플롯합니다. X 및 Y 좌표를 따라 세 개의 선과 X 및 Z 좌표를 따라 한 개의 선을 플롯합니다.

```python
# Plot edges
edges_kw = dict(color='0.4', linewidth=1, zorder=1e3)
ax.plot([xmax, xmax], [ymin, ymax], 0, **edges_kw)
ax.plot([xmin, xmax], [ymin, ymin], 0, **edges_kw)
ax.plot([xmax, xmax], [ymin, ymin], [zmin, zmax], **edges_kw)
```
