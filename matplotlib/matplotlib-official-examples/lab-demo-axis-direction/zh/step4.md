# 更改轴的方向

现在，我们将创建一个循环，以设置四个不同的绘图，每个绘图中的浮动轴位于四个基本方向中的一个。在循环中，我们将使用 `add_floating_axis1()` 和 `add_floating_axis2()` 添加浮动轴，并使用 `set_axis_direction()` 设置轴的方向。

```python
fig = plt.figure(figsize=(8, 4), layout="constrained")

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=241+i)
    axis = add_floating_axis1(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=245+i)
    axis = add_floating_axis2(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

plt.show()
```
