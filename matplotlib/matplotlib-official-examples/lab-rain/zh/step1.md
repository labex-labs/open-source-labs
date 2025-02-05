# 创建新的图形和坐标轴

第一步是创建一个新的图形以及填充该图形的坐标轴。这将是绘制模拟的画布。

```python
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
```
