# 应用谱共聚类算法

我们将谱共聚类算法应用于具有5个聚类的打乱后的数据集。

```python
model = SpectralCoclustering(n_clusters=5, random_state=0)
model.fit(data)
```
