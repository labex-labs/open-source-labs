# 加载数据集

我们将使用`sklearn.datasets`中的`make_gaussian_quantiles`函数来生成一个数据集。此函数生成各向同性高斯分布，并在类别之间添加分隔，以使问题更具挑战性。

```python
X, y = make_gaussian_quantiles(
    n_samples=13000, n_features=10, n_classes=3, random_state=1
)
```
