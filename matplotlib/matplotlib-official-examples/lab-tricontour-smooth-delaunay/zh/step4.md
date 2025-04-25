# 执行 Delaunay 三角剖分

我们使用 `matplotlib.tri` 模块中的 `Triangulation` 函数对测试数据点执行 Delaunay 三角剖分。

```python
# meshing with Delaunay triangulation
tri = Triangulation(x_test, y_test)
ntri = tri.triangles.shape[0]
```
