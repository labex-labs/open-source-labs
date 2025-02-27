# Crear conjuntos de datos

Crearemos tres conjuntos de datos con fines de visualización. El primer conjunto de datos será un conjunto aleatorio de 200 muestras de una distribución uniforme entre -3 y 3 en ambas dimensiones. El segundo conjunto de datos será un conjunto de 200 muestras generadas usando la función `make_blobs` de `sklearn.datasets`. El tercer conjunto de datos también se generará usando la función `make_blobs`.

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
