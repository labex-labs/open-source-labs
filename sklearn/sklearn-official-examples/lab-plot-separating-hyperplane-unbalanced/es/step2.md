# Crear datos

Vamos a crear dos clusters de puntos aleatorios utilizando la función `make_blobs`. Crearemos un cluster con 1000 puntos y otro con 100 puntos. Los centros de los clusters serán `[0.0, 0.0]` y `[2.0, 2.0]`, respectivamente. El parámetro `clusters_std` controla la desviación estándar de los clusters.

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
