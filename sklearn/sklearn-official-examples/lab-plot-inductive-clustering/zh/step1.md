# 生成训练数据

在这一步中，我们将通过聚类生成一些训练数据。我们将使用 scikit-learn 中的 `make_blobs` 函数来生成 5000 个样本，这些样本分为 3 个聚类，每个聚类具有不同的标准差和中心。

```python
X, y = make_blobs(
    n_samples=5000,
    cluster_std=[1.0, 1.0, 0.5],
    centers=[(-5, -5), (0, 0), (5, 5)],
    random_state=42,
)
```
