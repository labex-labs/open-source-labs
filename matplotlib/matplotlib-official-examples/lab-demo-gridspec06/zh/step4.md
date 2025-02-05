# 创建内部网格和子图

在这一步中，我们将使用嵌套的`.GridSpec`来创建内部网格和子图。我们将遍历外部网格中的每个单元格，并为每个单元格创建一个3x3的网格。

```python
for a in range(4):
    for b in range(4):
        # 网格规格嵌套在网格规格中
        inner_grid = outer_grid[a, b].subgridspec(3, 3, wspace=0, hspace=0)
        axs = inner_grid.subplots()  # 为内部网格创建所有子图。
        for (c, d), ax in np.ndenumerate(axs):
            ax.plot(*squiggle_xy(a + 1, b + 1, c + 1, d + 1))
            ax.set(xticks=[], yticks=[])
```
