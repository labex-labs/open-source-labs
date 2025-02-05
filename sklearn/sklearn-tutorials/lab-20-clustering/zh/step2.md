# 生成样本数据

接下来，让我们生成一些用于处理的样本数据。我们将使用 `sklearn.datasets` 模块中的 `make_blobs` 函数来创建一个带有聚类的合成数据集。

```python
# 生成样本数据
X, y = make_blobs(n_samples=100, centers=4, random_state=0, cluster_std=1.0)
```
