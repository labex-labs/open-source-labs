# 创建极坐标柱状图

我们将使用 `projection='polar'` 参数创建一个极坐标柱状图。

```python
ax = plt.subplot(projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)
```
