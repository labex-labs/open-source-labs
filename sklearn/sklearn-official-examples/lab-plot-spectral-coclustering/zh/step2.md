# 生成数据集

我们使用 `make_biclusters` 函数生成一个形状为 (300, 300) 的数据集，其中包含 5 个双聚类和 5 个噪声。

```python
data, rows, columns = make_biclusters(shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0)
```
