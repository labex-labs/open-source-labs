# 创建数据

我们将创建三个不同的数据集来说明t-SNE的用法。第一个数据集将是两个同心圆。

```python
n_samples = 150
n_components = 2

X, y = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05, random_state=0
)

red = y == 0
green = y == 1
```
