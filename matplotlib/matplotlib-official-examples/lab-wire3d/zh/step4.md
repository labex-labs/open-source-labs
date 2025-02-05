# 自定义绘图

我们可以对绘图进行自定义，使其在视觉上更具吸引力。在这个例子中，我们将添加一个标题、坐标轴标签，并更改绘图的颜色。

```python
# 自定义绘图
ax.set_title('线框绘图')
ax.set_xlabel('X 轴标签')
ax.set_ylabel('Y 轴标签')
ax.set_zlabel('Z 轴标签')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color='green')
```
