# 创建一个原点偏移的极坐标散点图

我们可以通过设置 `PolarAxes` 对象的 `set_rorigin()` 和 `set_theta_zero_location()` 方法，创建一个原点偏移的极坐标散点图。我们将把原点半径设置为 `-2.5`，并将 theta 零点位置设置为 `'W'`，偏移量为 `10`。

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_rorigin(-2.5)
ax.set_theta_zero_location('W', offset=10)
```
