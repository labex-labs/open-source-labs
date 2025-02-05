# 创建带有多种阴影线的柱状图

你也可以在柱状图中使用多种阴影线。在这种情况下，我们将使用一个阴影线数组在柱子上创建多种阴影线。

```python
plt.bar(x, y1, edgecolor='black', hatch=['--', '+', 'x', '\\'])
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch=['*', 'o', 'O', '.'])
```
