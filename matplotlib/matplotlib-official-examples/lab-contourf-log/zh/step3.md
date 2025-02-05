# 创建图表

我们将使用`contourf`函数创建一个具有对数颜色刻度的填充等高线图：

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

cbar = fig.colorbar(cs)

plt.show()
```
