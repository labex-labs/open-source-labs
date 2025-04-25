# 为每个主要的 3D 视图平面添加标签

我们使用步骤 2 中定义的 `annotate_axes` 函数，为每个主要的 3D 视图平面标注其各自的角度。

```python
for plane, angles in views:
    label = f'{plane}\n{angles}'
    annotate_axes(axd[plane], label, fontsize=14)
```
