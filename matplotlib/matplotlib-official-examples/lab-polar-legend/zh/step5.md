# 自定义绘图

我们可以通过更改网格颜色和添加图例来自定义绘图。在本示例中，我们将把图例稍微移离绘图中心以避免重叠。

```python
ax.tick_params(grid_color="palegoldenrod")
angle = np.deg2rad(67.5)
ax.legend(loc="lower left",
          bbox_to_anchor=(.5 + np.cos(angle)/2,.5 + np.sin(angle)/2))
```
