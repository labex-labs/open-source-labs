# 创建 3D 图

我们使用 `subplot_mosaic` 根据步骤 4 中定义的布局来创建 3D 图。

```python
fig, axd = plt.subplot_mosaic(layout, subplot_kw={'projection': '3d'},
                              figsize=(12, 8.5))
```
