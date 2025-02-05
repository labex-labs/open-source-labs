# 创建 3D 等高线图

我们将使用创建的三角剖分和 z 坐标来创建一个 3D 等高线图。我们还将自定义视角，以便更易于理解该图。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontour(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)
plt.show()
```
