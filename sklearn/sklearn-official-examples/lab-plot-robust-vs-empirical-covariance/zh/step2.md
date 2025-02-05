# 生成数据

在这一步中，我们生成一个具有 `n_samples` 个样本和 `n_features` 个特征的随机数据集。我们还向数据集中添加了一些异常值。

```python
n_samples = 80
n_features = 5

# 生成随机数据集
rng = np.random.RandomState(42)
X = rng.randn(n_samples, n_features)

# 向数据集中添加异常值
n_outliers = 20
异常值索引 = rng.permutation(n_samples)[:n_outliers]
异常值偏移量 = 10.0 * (
    np.random.randint(2, size=(n_outliers, n_features)) - 0.5
)
X[异常值索引] += 异常值偏移量
```
