# 在 x 轴上创建对称对数图

在第一个子图中，我们将在 x 轴上创建一个对称对数图。我们还将为 x 轴添加一个次要网格。

```python
ax0.plot(x, y1)
ax0.set_xscale('symlog')
ax0.set_ylabel('symlogx')
ax0.grid()
ax0.xaxis.grid(which='minor')
```
