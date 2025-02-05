# 自定义箭头以连接到椭圆

在这一步中，我们将自定义箭头以连接到椭圆。我们将使用 `arrowprops` 参数来指定箭头应连接到椭圆，并且我们还将自定义箭头的样式和颜色。

```python
ax = axs.flat[2]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            patchB=el,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
