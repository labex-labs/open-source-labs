# 生成样本数据

接下来，我们将使用 `sklearn.datasets` 模块中的 `make_blobs` 函数生成样本数据。我们将创建一个包含 10,000 个样本的数据集，该数据集有三个聚类中心，分别为 `[[1, 1], [-1, -1], [1, -1]]`，标准差为 0.6。

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
```
