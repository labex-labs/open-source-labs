# 自定义图表

我们可以通过添加标签、标题以及更改颜色映射来自定义图表：

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.coolwarm)

ax.set_title('Contourf Plot with Log Color Scale')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

cbar = fig.colorbar(cs)

plt.show()
```
