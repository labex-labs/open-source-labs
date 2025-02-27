# Datensätze generieren

Wir werden einen Datensatz von isotopen Gaußschen Clustern mit großer Abstand generieren. Die Parameter für die Datensatzgenerierung umfassen die Anzahl der Proben pro Zentrum, die Gittergröße, die Skala und die Anzahl der Cluster.

```python
random_state = np.random.RandomState(0)
n_samples_per_center = 100
grid_size = 3
scale = 0.1
n_clusters = grid_size**2

def make_data(random_state, n_samples_per_center, grid_size, scale):
    random_state = check_random_state(random_state)
    centers = np.array([[i, j] for i in range(grid_size) for j in range(grid_size)])
    n_clusters_true, n_features = centers.shape

    noise = random_state.normal(
        scale=scale, size=(n_samples_per_center, centers.shape[1])
    )

    X = np.concatenate([c + noise for c in centers])
    y = np.concatenate([[i] * n_samples_per_center for i in range(n_clusters_true)])
    return shuffle(X, y, random_state=random_state)

X, y = make_data(random_state, n_samples_per_center, grid_size, scale)
```
