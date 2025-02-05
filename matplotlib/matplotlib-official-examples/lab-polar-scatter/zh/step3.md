# 在极坐标轴上创建散点图

我们将使用 `plt.scatter()` 函数在极坐标轴上创建一个散点图。我们会将 `projection` 参数设置为 `'polar'`，并将半径、角度、颜色和面积值作为参数传入。

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
```
