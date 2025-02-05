# 创建图形和坐标轴

接下来，我们将使用 `subplots()` 方法创建一个图形和坐标轴。然后，我们将在坐标轴上绘制两条线，并添加一个图例以区分它们。

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```
