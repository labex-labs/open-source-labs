# 创建极坐标图

接下来，我们通过定义图形并指定其具有极坐标投影来创建极坐标图。我们还定义了用于绘图的半径和 theta 值。

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r
line, = ax.plot(theta, r, color='#ee8d18', lw=3)
```
