# 构建数据集

在这一步中，我们将使用 `sklearn.datasets` 模块中的 `make_gaussian_quantiles` 函数创建一个由两个高斯分位数簇组成的非线性可分分类数据集。我们还将把这两个簇连接起来并为它们分配标签。

```python
X1, y1 = make_gaussian_quantiles(
    cov=2.0, n_samples=200, n_features=2, n_classes=2, random_state=1
)
X2, y2 = make_gaussian_quantiles(
    mean=(3, 3), cov=1.5, n_samples=300, n_features=2, n_classes=2, random_state=1
)
X = np.concatenate((X1, X2))
y = np.concatenate((y1, -y2 + 1))
```
