# 创建带阴影线的柱状图

既然你已经有了数据，就可以创建一个带阴影线的柱状图。你可以使用阴影线在图表的柱子上创建图案。在这种情况下，我们将使用`hatch`参数为柱子添加阴影线。

```python
plt.bar(x, y1, edgecolor='black', hatch="/")
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch='//')
```
