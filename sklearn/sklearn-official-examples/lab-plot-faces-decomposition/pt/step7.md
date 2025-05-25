# Centros de Clusters - MiniBatchKMeans

O agrupamento K-means é um método para particionar um conjunto de dados em clusters, minimizando a soma dos quadrados das distâncias entre cada ponto e o centroide do cluster atribuído. Aplicamos o MiniBatchKMeans, uma versão mais rápida do KMeans, mais adequada para conjuntos de dados grandes.

```python
# Centros de Clusters - MiniBatchKMeans
kmeans_estimator = cluster.MiniBatchKMeans(
    n_clusters=n_components,
    tol=1e-3,
    batch_size=20,
    max_iter=50,
    random_state=rng,
    n_init="auto",
)
kmeans_estimator.fit(faces_centered)
plot_gallery(
    "Centros de Clusters - MiniBatchKMeans",
    kmeans_estimator.cluster_centers_[:n_components],
)
```
