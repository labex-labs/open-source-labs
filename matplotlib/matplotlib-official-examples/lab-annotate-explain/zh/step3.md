# 在图表中添加椭圆

在这一步中，我们将在图表中添加一个椭圆。我们将使用 `Ellipse` 函数来创建椭圆，并自定义椭圆的属性，如位置、宽度、高度和角度。

```python
ax = axs.flat[1]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
```
