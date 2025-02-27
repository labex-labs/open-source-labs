# Daten erstellen

Wir werden zwei Cluster von zufälligen Punkten mit der `make_blobs`-Funktion erstellen. Wir werden einen Cluster mit 1000 Punkten und einen anderen mit 100 Punkten erstellen. Die Mittelpunkte der Cluster werden jeweils `[0.0, 0.0]` und `[2.0, 2.0]` sein. Der Parameter `clusters_std` steuert die Standardabweichung der Cluster.

```python
n_samples_1 = 1000
n_samples_2 = 100
centers = [[0.0, 0.0], [2.0, 2.0]]
clusters_std = [1.5, 0.5]
X, y = make_blobs(
    n_samples=[n_samples_1, n_samples_2],
    centers=centers,
    cluster_std=clusters_std,
    random_state=0,
    shuffle=False,
)
```
