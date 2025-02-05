# 生成样本数据

我们将使用 scikit-learn 库的 `make_blobs` 函数来生成样本数据。此函数生成用于聚类的各向同性高斯数据点集。我们将生成 4000 个样本，有 4 个聚类中心。

```python
# 生成样本数据
n_samples = 4000
n_components = 4

X, y_true = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)
X = X[:, ::-1]
```
