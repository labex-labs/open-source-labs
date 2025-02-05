# 添加一个内嵌图

在这一步中，我们将向主图中添加一个内嵌图。这个内嵌图将展示主图的一个放大区域。

```python
# inset axes....
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9  # 原始图像的子区域
axins = ax.inset_axes(
    [0.5, 0.5, 0.47, 0.47],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
axins.imshow(Z2, extent=extent, origin="lower")
```
