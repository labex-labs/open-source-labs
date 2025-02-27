# Centres de grappe - MiniBatchKMeans

Le regroupement K-moyennes est une méthode pour partitionner un ensemble de données en grappes en minimisant la somme des distances carrées entre chaque point et le centroïde de la grappe à laquelle il est assigné. Nous appliquons MiniBatchKMeans, qui est une version plus rapide de KMeans qui est mieux adaptée aux grands jeux de données.

```python
# Centres de grappe - MiniBatchKMeans
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
    "Centres de grappe - MiniBatchKMeans",
    kmeans_estimator.cluster_centers_[:n_components],
)
```
