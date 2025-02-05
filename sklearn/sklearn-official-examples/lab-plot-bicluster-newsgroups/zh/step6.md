# 使用谱共聚类算法进行双聚类

我们将通过定义共聚类并将其拟合到数据上来使用谱共聚类算法执行双聚类。

```python
cocluster = SpectralCoclustering(
    n_clusters=len(categories), svd_method="arpack", random_state=0
)
cocluster.fit(X)
y_cocluster = cocluster.row_labels_
```
