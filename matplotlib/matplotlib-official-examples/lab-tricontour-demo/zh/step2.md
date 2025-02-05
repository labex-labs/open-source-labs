# 创建三角剖分

我们将使用 `matplotlib.tri.Triangulation` 创建三角剖分。我们不需要指定三角形，因此将自动创建点的德劳内三角剖分。

```python
triang = tri.Triangulation(x, y)
```
