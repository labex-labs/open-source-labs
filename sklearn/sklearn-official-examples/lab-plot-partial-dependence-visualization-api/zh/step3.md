# 一起绘制两个模型的局部依赖关系

在这一步中，我们将在同一张图上绘制两个模型的局部依赖曲线。

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
tree_disp.plot(ax=ax1)
ax1.set_title("决策树")
mlp_disp.plot(ax=ax2, line_kw={"color": "red"})
ax2.set_title("多层感知器")
```

另一种比较曲线的方法是将它们绘制在彼此之上。在这里，我们创建一个一行两列的图形。轴作为列表传递给 `PartialDependenceDisplay.plot` 函数，该函数将在同一轴上绘制每个模型的局部依赖曲线。轴列表的长度必须等于绘制的图的数量。

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
tree_disp.plot(ax=[ax1, ax2], line_kw={"label": "决策树"})
mlp_disp.plot(
    ax=[ax1, ax2], line_kw={"label": "多层感知器", "color": "red"}
)
ax1.legend()
ax2.legend()
```

`tree_disp.axes_` 是一个numpy数组，包含用于绘制局部依赖图的轴。这可以传递给 `mlp_disp`，以产生将图绘制在彼此之上的相同效果。此外，`mlp_disp.figure_` 存储图形，这允许在调用 `plot` 后调整图形大小。在这种情况下，`tree_disp.axes_` 有两个维度，因此 `plot` 只会在最左边的图上显示y标签和y刻度。

```python
tree_disp.plot(line_kw={"label": "决策树"})
mlp_disp.plot(
    line_kw={"label": "多层感知器", "color": "red"}, ax=tree_disp.axes_
)
tree_disp.figure_.set_size_inches(10, 6)
tree_disp.axes_[0, 0].legend()
tree_disp.axes_[0, 1].legend()
plt.show()
```
