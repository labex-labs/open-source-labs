# Tracer le résultat

Nous allons tracer les groupes résultants à l'aide de la bibliothèque `matplotlib`. Nous allons parcourir chaque groupe et tracer les points appartenant à ce groupe, ainsi que le centre du groupe et les lignes reliant le centre à chaque point du groupe.

```python
plt.close("all")
plt.figure(1)
plt.clf()

colors = plt.cycler("color", plt.cm.viridis(np.linspace(0, 1, 4)))

for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center = X[cluster_centers_indices[k]]
    plt.scatter(
        X[class_members, 0], X[class_members, 1], color=col["color"], marker="."
    )
    plt.scatter(
        cluster_center[0], cluster_center[1], s=14, color=col["color"], marker="o"
    )
    for x in X[class_members]:
        plt.plot(
            [cluster_center[0], x[0]], [cluster_center[1], x[1]], color=col["color"]
        )

plt.title("Nombre estimé de groupes : %d" % n_clusters_)
plt.show()
```
