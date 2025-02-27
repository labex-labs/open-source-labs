# Clusterzentren - MiniBatchKMeans

Das K-Means-Clustering ist eine Methode, um einen Datensatz in Cluster zu unterteilen, indem die Summe der quadrierten Abstände zwischen jedem Punkt und dem Schwerpunkt seines zugewiesenen Clusters minimiert wird. Wir wenden MiniBatchKMeans an, was eine schnellere Version von KMeans ist und für große Datensätze besser geeignet ist.

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
