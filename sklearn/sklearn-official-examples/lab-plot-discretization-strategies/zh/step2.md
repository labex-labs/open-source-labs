# 创建数据集

为了便于可视化，我们将创建三个数据集。第一个数据集是一个随机集合，包含 200 个样本，其两个维度均服从 -3 到 3 之间的均匀分布。第二个数据集是使用`sklearn.datasets`中的`make_blobs`函数生成的 200 个样本集合。第三个数据集同样使用`make_blobs`函数生成。

```python
n_samples = 200
centers_0 = np.array([[0, 0], [0, 5], [2, 4], [8, 8]])
centers_1 = np.array([[0, 0], [3, 1]])

X_list = [
    np.random.RandomState(42).uniform(-3, 3, size=(n_samples, 2)),
    make_blobs(
        n_samples=[n_samples // 10, n_samples * 4 // 10, n_samples // 10, n_samples * 4 // 10],
        cluster_std=0.5,
        centers=centers_0,
        random_state=42,
    )[0],
    make_blobs(
        n_samples=[n_samples // 5, n_samples * 4 // 5],
        cluster_std=0.5,
        centers=centers_1,
        random_state=42,
    )[0],
]
```
