# Clustering-Algorithmus trainieren

In diesem Schritt werden wir einen Clustering-Algorithmus auf den generierten Trainingsdaten trainieren und die Clusterlabels erhalten. Wir werden `AgglomerativeClustering` aus scikit-learn verwenden, um den Algorithmus mit 3 Clustern zu trainieren.

```python
clusterer = AgglomerativeClustering(n_clusters=3)
cluster_labels = clusterer.fit_predict(X)
```
