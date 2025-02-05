# 设置缩放比例和视角

使用 `view_init` 和 `set_box_aspect` 方法设置缩放比例和视角。我们将把视角设置为在 X 方向上 40 度，在 Y 方向上 -30 度，并且将缩放比例设置为 0.9。

```python
# 设置缩放比例和视角
ax.view_init(40, -30, 0)
ax.set_box_aspect(None, zoom=0.9)
```
