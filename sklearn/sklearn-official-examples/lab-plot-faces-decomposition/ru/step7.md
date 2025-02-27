# Центры кластеров - MiniBatchKMeans

Алгоритм k - means кластеризации - это метод разделения набора данных на кластеры путем минимизации суммы квадратов расстояний между каждой точкой и центроидом ее назначенного кластера. Мы применяем MiniBatchKMeans, которая представляет собой более быструю версию KMeans, лучше подходящую для обработки больших наборов данных.

```python
# Cluster centers - MiniBatchKMeans
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
    "Cluster centers - MiniBatchKMeans",
    kmeans_estimator.cluster_centers_[:n_components],
)
```
