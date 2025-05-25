# Agrupamento Hierárquico Não Estruturado

Realizamos o `AgglomerativeClustering`, que se enquadra no Agrupamento Hierárquico sem quaisquer restrições de conectividade.

```python
from sklearn.cluster import AgglomerativeClustering

ward = AgglomerativeClustering(n_clusters=6, linkage="ward").fit(X)
label = ward.labels_
```
