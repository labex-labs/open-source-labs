# `SpectralBiclustering`を適合させる

モデルを適合させ、得られたクラスタと正解とを比較します。モデルを作成する際には、データセットを作成する際に使用したクラスタ数と同じ数を指定します（`n_clusters = (4, 3)`）。これが良好な結果を得るために役立ちます。

```python
from sklearn.cluster import SpectralBiclustering
from sklearn.metrics import consensus_score

model = SpectralBiclustering(n_clusters=n_clusters, method="log", random_state=0)
model.fit(data)

# Compute the similarity of two sets of biclusters
score = consensus_score(
    model.biclusters_, (rows[:, row_idx_shuffled], columns[:, col_idx_shuffled])
)
print(f"consensus score: {score:.1f}")
```
