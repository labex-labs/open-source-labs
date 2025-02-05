# 创建绘图

现在，我们将使用 `tricontourf()` 函数创建绘图并自定义视角。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontourf(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)

plt.show()
```
