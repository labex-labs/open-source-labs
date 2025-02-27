# Zeichnen des Ergebnisses

Wir werden die resultierenden Cluster mit der Bibliothek `matplotlib` zeichnen. Wir werden durch jeden Cluster iterieren und die zu diesem Cluster gehörenden Punkte zeichnen, zusammen mit dem Clusterzentrum und den Linien, die das Zentrum mit jedem Punkt im Cluster verbinden.

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

plt.title("Geschätzte Anzahl der Cluster: %d" % n_clusters_)
plt.show()
```
