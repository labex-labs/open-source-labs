# Entraîner un algorithme de classification

Dans cette étape, nous allons entraîner un algorithme de classification sur les données d'entraînement générées et obtenir les étiquettes de clusters. Nous utiliserons `AgglomerativeClustering` de scikit-learn pour entraîner l'algorithme avec 3 clusters.

```python
clusterer = AgglomerativeClustering(n_clusters=3)
cluster_labels = clusterer.fit_predict(X)
```
