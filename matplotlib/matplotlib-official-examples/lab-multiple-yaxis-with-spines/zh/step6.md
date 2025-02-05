# 设置轴的范围和标签

我们使用 `set` 方法为每个 y 轴设置范围和标签。我们还使用 `set_color` 方法将标签的颜色设置为与线条颜色匹配。

```python
ax.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
twin1.set(ylim=(0, 4), ylabel="Temperature")
twin2.set(ylim=(1, 65), ylabel="Velocity")

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())
twin2.yaxis.label.set_color(p3.get_color())
```
