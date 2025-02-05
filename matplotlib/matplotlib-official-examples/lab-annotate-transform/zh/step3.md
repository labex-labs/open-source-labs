# 创建图表

现在，我们将使用 `matplotlib.pyplot` 库来创建图表。我们将设置图表的 x 轴和 y 轴范围，然后绘制数据。

```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
```
