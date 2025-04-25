# 创建数据

我们将使用 `make_blobs` 函数创建两个随机点簇。我们将创建一个包含 1000 个点的簇和另一个包含 100 个点的簇。簇的中心将分别为 `[0.0, 0.0]` 和 `[2.0, 2.0]`。`clusters_std` 参数控制簇的标准差。

```python
n_samples_1 = 1000
n_samples_2 = 100
centers = [[0.0, 0.0], [2.0, 2.0]]
clusters_std = [1.5, 0.5]
X, y = make_blobs(
    n_samples=[n_samples_1, n_samples_2],
    centers=centers,
    cluster_std=clusters_std,
    random_state=0,
    shuffle=False,
)
```
