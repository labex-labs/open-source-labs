# Plotar Resultados

Finalmente, plotaremos os resultados usando a biblioteca `matplotlib.pyplot`. Usaremos cores e marcadores diferentes para cada cluster, e também plotaremos os centros dos clusters.

```python
plt.figure(1)
plt.clf()

colors = ["#dede00", "#377eb8", "#f781bf"]
markers = ["x", "o", "^"]

for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    plt.plot(X[my_members, 0], X[my_members, 1], markers[k], color=col)
    plt.plot(
        cluster_center[0],
        cluster_center[1],
        markers[k],
        markerfacecolor=col,
        markeredgecolor="k",
        markersize=14,
    )
plt.title("Número estimado de clusters: %d" % n_clusters_)
plt.show()
```
