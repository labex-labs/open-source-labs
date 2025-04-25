# 将图像转换为边带有梯度值的图

我们将把图像转换为边带有梯度值的图。β值越小，分割结果对实际图像的依赖性就越低。当β = 1 时，分割结果接近沃罗诺伊图（Voronoi diagram）。

```python
# 将图像转换为边带有梯度值的图。
graph = image.img_to_graph(rescaled_coins)

# 对梯度取一个递减函数：指数函数
beta = 10
eps = 1e-6
graph.data = np.exp(-beta * graph.data / graph.data.std()) + eps
```
