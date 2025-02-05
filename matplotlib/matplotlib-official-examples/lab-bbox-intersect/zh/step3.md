# 生成随机线条

我们将使用 `numpy` 库生成 12 条随机线条，并使用 `plot` 方法绘制它们。如果一条线与矩形相交，它的颜色将为红色，否则为蓝色。我们将使用 `Path` 类创建一条线，并使用 `intersects_bbox` 方法检查它是否与矩形相交。

```python
bbox = Bbox.from_bounds(left, bottom, width, height)

for i in range(12):
    vertices = (np.random.random((2, 2)) - 0.5) * 6.0
    path = Path(vertices)
    if path.intersects_bbox(bbox):
        color = 'r'
    else:
        color = 'b'
    ax.plot(vertices[:, 0], vertices[:, 1], color=color)
```
