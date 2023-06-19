# Cluster centers - MiniBatchKMeans

K-means clustering is a method for partitioning a dataset into clusters by minimizing the sum of squared distances between each point and the centroid of its assigned cluster. We apply MiniBatchKMeans, which is a faster version of KMeans that is better suited for large datasets.

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
