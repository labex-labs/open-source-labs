# 创建一个限制在扇形区域内的极坐标散点图

我们可以通过设置 `PolarAxes` 对象的 `set_thetamin()` 和 `set_thetamax()` 方法，在极坐标轴上创建一个限制在扇形区域内的散点图。我们将分别把 theta 的起始和结束限制设置为 `45` 和 `135`。

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_thetamin(45)
ax.set_thetamax(135)
```
