# Biclustering mit dem Spektralen Co-Clustering-Algorithmus

Wir werden Biclustering mit dem Spektralen Co-Clustering-Algorithmus durch die Definition eines Co-Clusters und das Anpassen an die Daten durchführen.

```python
cocluster = SpectralCoclustering(
    n_clusters=len(categories), svd_method="arpack", random_state=0
)
cocluster.fit(X)
y_cocluster = cocluster.row_labels_
```
