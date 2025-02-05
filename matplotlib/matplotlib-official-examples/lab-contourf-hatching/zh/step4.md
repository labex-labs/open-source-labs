# 无颜色阴影且带图例的绘图

在这一步中，我们将创建一个无颜色阴影的绘图并添加一个图例。我们将使用 `contour` 函数来创建等高线，使用 `contourf` 函数来指定无颜色的阴影。

```python
fig2, ax2 = plt.subplots()
n_levels = 6
ax2.contour(x, y, z, n_levels, colors='black', linestyles='-')
cs = ax2.contourf(x, y, z, n_levels, colors='none',
                  hatches=['.', '/', '\\', None, '\\\\', '*'],
                  extend='lower')

# 为等高线集创建一个图例
artists, labels = cs.legend_elements(str_format='{:2.1f}'.format)
ax2.legend(artists, labels, handleheight=2, framealpha=1)
```
