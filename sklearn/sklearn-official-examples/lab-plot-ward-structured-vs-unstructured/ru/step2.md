# Неструктурированная иерархическая кластеризация

Выполняем AgglomerativeClustering, которая относится к иерархической кластеризации без каких-либо ограничений связности.

```python
from sklearn.cluster import AgglomerativeClustering

ward = AgglomerativeClustering(n_clusters=6, linkage="ward").fit(X)
label = ward.labels_
```
