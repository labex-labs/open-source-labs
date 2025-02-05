# 设置标签和 Z 轴刻度

使用 `set` 方法设置标签和 Z 轴刻度。我们将设置 X、Y 和 Z 坐标的标签，并设置 Z 轴刻度以显示盒子的深度。

```python
# 设置标签和 Z 轴刻度
ax.set(
    xlabel='X [km]',
    ylabel='Y [km]',
    zlabel='Z [m]',
    zticks=[0, -150, -300, -450],
)
```
