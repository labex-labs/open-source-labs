# Appliquer le regroupement K-Means

Maintenant, nous allons appliquer l'algorithme de regroupement K-Means à nos données. Nous allons initialiser l'algorithme avec 3 clusters et l'ajuster à nos données.

```python
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
```
