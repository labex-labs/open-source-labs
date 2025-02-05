# 创建一个内嵌轴

使用 `zoomed_inset_axes` 函数创建一个内嵌轴。设置缩放级别以及内嵌轴在主图中的位置。

```python
axins = zoomed_inset_axes(ax, zoom=2, loc='upper left')
axins.set(xticks=[], yticks=[])
```
