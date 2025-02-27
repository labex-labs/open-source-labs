# Création d'ensembles de données

Nous allons créer trois ensembles de données à des fins de visualisation. Le premier ensemble de données sera un ensemble aléatoire de 200 échantillons provenant d'une distribution uniforme entre -3 et 3 dans les deux dimensions. Le second ensemble de données sera un ensemble de 200 échantillons générés à l'aide de la fonction `make_blobs` de `sklearn.datasets`. Le troisième ensemble de données sera également généré à l'aide de la fonction `make_blobs`.

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
