# 创建图表

现在我们准备好创建图表了。我们将使用 Matplotlib 的 `plot` 函数在同一图表上绘制三条线，每条线都有一个预定义的标签。我们将使用 `label` 参数为每条线分配标签。

```python
# 创建带有预定义标签的图表。
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')
```
