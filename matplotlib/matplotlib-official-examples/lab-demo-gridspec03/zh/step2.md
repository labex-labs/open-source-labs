# 使用 `GridSpec` 生成子图

在这一步中，我们将使用 `GridSpec` 来生成子图。我们将创建一个 2 行 2 列的图形。我们还将指定 `width_ratios` 和 `height_ratios` 来控制子图的相对大小。

```python
fig = plt.figure()
gs = GridSpec(2, 2, width_ratios=[1, 2], height_ratios=[4, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])
ax4 = fig.add_subplot(gs[3])
```
