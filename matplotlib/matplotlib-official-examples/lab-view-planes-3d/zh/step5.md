# 创建3D图

我们使用 `subplot_mosaic` 根据步骤4中定义的布局来创建3D图。

```python
fig, axd = plt.subplot_mosaic(layout, subplot_kw={'projection': '3d'},
                              figsize=(12, 8.5))
```
