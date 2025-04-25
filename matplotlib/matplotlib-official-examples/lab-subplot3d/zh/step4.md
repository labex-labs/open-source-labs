# 创建三维线框图

我们将为第二个子图创建一个三维线框图。我们将使用 mpl_toolkits.mplot3d.axes3d 中的`get_test_data`函数来创建该图的数据。

```python
# 为三维线框图创建数据
X, Y, Z = Axes3D.get_test_data(0.05)

# 绘制三维线框图
ax2.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
