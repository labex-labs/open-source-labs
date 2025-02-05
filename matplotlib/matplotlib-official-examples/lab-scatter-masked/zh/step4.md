# 添加一条线来划分屏蔽区域

最后，我们添加一条线来划分屏蔽区域。我们创建一个theta值的数组，并使用 `np.cos(theta)` 和 `np.sin(theta)` 绘制一个半径为 `r0` 的圆。

```python
# 显示区域之间的边界：
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))
```
