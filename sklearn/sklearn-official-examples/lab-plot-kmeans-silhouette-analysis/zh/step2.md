# 生成数据

我们将使用 `sklearn.datasets` 库中的 `make_blobs` 函数来生成样本数据。此函数生成用于聚类的各向同性高斯数据点集。

```python
X, y = make_blobs(
    n_samples=500,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=1,
)  # For reproducibility
```
