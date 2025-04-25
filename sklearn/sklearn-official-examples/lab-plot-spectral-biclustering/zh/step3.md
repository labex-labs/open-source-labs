# 拟合“谱双聚类（SpectralBiclustering）”

我们拟合模型，并将得到的聚类结果与真实情况进行比较。请注意，在创建模型时，我们指定了与用于创建数据集相同数量的聚类（`n_clusters = (4, 3)`），这将有助于获得良好的结果。

```python
from sklearn.cluster import SpectralBiclustering
from sklearn.metrics import consensus_score

model = SpectralBiclustering(n_clusters=n_clusters, method="log", random_state=0)
model.fit(data)

# 计算两组双聚类的相似度
score = consensus_score(
    model.biclusters_, (rows[:, row_idx_shuffled], columns[:, col_idx_shuffled])
)
print(f"一致性得分：{score:.1f}")
```
