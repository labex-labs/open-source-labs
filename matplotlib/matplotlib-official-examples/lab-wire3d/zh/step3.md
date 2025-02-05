# 创建绘图

既然我们已经有了数据，就可以创建线框绘图了。在这个例子中，我们将使用 `plot_wireframe()` 函数来创建绘图。

```python
# 创建绘图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
```
