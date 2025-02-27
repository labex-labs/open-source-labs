# Visualiser les résultats

Dans cette étape, nous allons visualiser les résultats des algorithmes à l'aide de sous-graphiques. Nous utiliserons le nuage de points pour représenter les points de données et les centroïdes de cluster. Nous allons itérer sur chaque algorithme et le nombre de clusters à comparer et tracer les résultats.

```python
fig, axs = plt.subplots(len(clustering_algorithms), len(n_clusters_list), figsize=(12, 5))
axs = axs.T

for i, (algorithm_name, Algorithm) in enumerate(clustering_algorithms.items()):
    for j, n_clusters in enumerate(n_clusters_list):
        algo = Algorithm(n_clusters=n_clusters, random_state=random_state, n_init=3)
        algo.fit(X)
        centers = algo.cluster_centers_

        axs[j, i].scatter(X[:, 0], X[:, 1], s=10, c=algo.labels_)
        axs[j, i].scatter(centers[:, 0], centers[:, 1], c="r", s=20)

        axs[j, i].set_title(f"{algorithm_name} : {n_clusters} clusters")

for ax in axs.flat:
    ax.label_outer()
    ax.set_xticks([])
    ax.set_yticks([])

plt.show()
```
