# 绘制表面

最后，我们使用 `plot_trisurf()` 函数绘制表面。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)
```
