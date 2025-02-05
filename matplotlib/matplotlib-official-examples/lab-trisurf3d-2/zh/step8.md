# 创建三角剖分

我们使用 `Triangulation()` 函数创建三角剖分。由于没有预先指定三角形，因此会创建德劳内三角剖分（Delaunay triangulation）。

```python
triang = mtri.Triangulation(x, y)
```
