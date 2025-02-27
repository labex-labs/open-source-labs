# Centros de clúster - MiniBatchKMeans

El algoritmo de clustering K-means es un método para particionar un conjunto de datos en clústeres minimizando la suma de las distancias al cuadrado entre cada punto y el centroide de su clúster asignado. Aplicamos MiniBatchKMeans, que es una versión más rápida de KMeans que es más adecuada para conjuntos de datos grandes.

```python
# Centros de clúster - MiniBatchKMeans
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
    "Centros de clúster - MiniBatchKMeans",
    kmeans_estimator.cluster_centers_[:n_components],
)
```
