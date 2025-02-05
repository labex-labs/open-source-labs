# 生成示例数据

我们将使用 `sklearn.datasets` 模块中的 `make_blobs` 函数生成一个示例数据集。`make_blobs` 函数在 n 维空间中生成一个点的数据集，每个点属于 k 个聚类之一。我们将在二维空间中生成一个包含 300 个点的数据集，有 3 个聚类，标准差为 0.5。

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.5, random_state=0
)
```
