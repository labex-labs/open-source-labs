# スペクトラルクラスタリング

`sklearn.cluster` の `spectral_clustering` 関数を使って、スペクトラルクラスタリングを行います。4 つの円を分離するために、`n_clusters` パラメータを 4 に設定します。

```python
from sklearn.cluster import spectral_clustering

labels = spectral_clustering(graph, n_clusters=4, eigen_solver="arpack")
```
