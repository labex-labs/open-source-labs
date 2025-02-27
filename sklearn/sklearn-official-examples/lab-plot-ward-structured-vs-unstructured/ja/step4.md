# 構造化階層的クラスタリング

Scikit-learnの`kneighbors_graph`関数を使って、10個の近傍点を持つk近傍法（k-Nearest Neighbors）を定義します。

```python
from sklearn.neighbors import kneighbors_graph

connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)
```

接続制約付きで再び凝集型クラスタリング（AgglomerativeClustering）を行います。

```python
ward = AgglomerativeClustering(
    n_clusters=6, connectivity=connectivity, linkage="ward"
).fit(X)
label = ward.labels_
```
