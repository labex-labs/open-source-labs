# 生成样本数据

在这一步中，我们将使用 scikit-learn 中的 `make_blobs()` 函数生成样本数据。我们将生成 10000 个样本，有 2 个聚类中心。

```python
n_samples = 10000
random_state = 0
X, _ = make_blobs(n_samples=n_samples, centers=2, random_state=random_state)
```
