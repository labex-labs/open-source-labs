# 非構造化階層的クラスタリング

接続制約なしで階層的クラスタリングに属する凝集型クラスタリング（AgglomerativeClustering）を行います。

```python
from sklearn.cluster import AgglomerativeClustering

ward = AgglomerativeClustering(n_clusters=6, linkage="ward").fit(X)
label = ward.labels_
```
