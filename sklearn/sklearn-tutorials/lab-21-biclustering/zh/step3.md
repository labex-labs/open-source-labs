# 执行谱双聚类

接下来，让我们使用谱双聚类算法进行双聚类。该算法假设数据矩阵具有隐藏的棋盘结构。

```python
# Initialize and fit the Spectral Biclustering model
model_bi = SpectralBiclustering(n_clusters=(2, 3), random_state=0)
model_bi.fit(data)

# Get row and column cluster membership
row_clusters_bi = model_bi.row_labels_
column_clusters_bi = model_bi.column_labels_
```
