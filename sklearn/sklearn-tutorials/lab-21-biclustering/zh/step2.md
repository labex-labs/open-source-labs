# 执行谱共聚类

现在，让我们使用谱共聚类算法进行双聚类。该算法会找到与其他行和列相比具有更高值的双聚类。

```python
# Initialize and fit the Spectral Co-Clustering model
model_co = SpectralCoclustering(n_clusters=3, random_state=0)
model_co.fit(data)

# Get row and column cluster membership
row_clusters_co = model_co.row_labels_
column_clusters_co = model_co.column_labels_
```
