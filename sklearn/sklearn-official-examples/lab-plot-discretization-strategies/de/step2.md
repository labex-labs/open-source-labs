# Datensätze erstellen

Wir werden drei Datensätze für die Visualisierung erstellen. Der erste Datensatz wird eine Zufallsmenge von 200 Proben aus einer gleichmäßigen Verteilung zwischen -3 und 3 in beiden Dimensionen sein. Der zweite Datensatz wird eine Menge von 200 Proben sein, die mit der Funktion `make_blobs` aus `sklearn.datasets` generiert werden. Der dritte Datensatz wird ebenfalls mit der Funktion `make_blobs` generiert werden.

```python
n_samples = 200
centers_0 = np.array([[0, 0], [0, 5], [2, 4], [8, 8]])
centers_1 = np.array([[0, 0], [3, 1]])

X_list = [
    np.random.RandomState(42).uniform(-3, 3, size=(n_samples, 2)),
    make_blobs(
        n_samples=[n_samples // 10, n_samples * 4 // 10, n_samples // 10, n_samples * 4 // 10],
        cluster_std=0.5,
        centers=centers_0,
        random_state=42,
    )[0],
    make_blobs(
        n_samples=[n_samples // 5, n_samples * 4 // 5],
        cluster_std=0.5,
        centers=centers_1,
        random_state=42,
    )[0],
]
```
