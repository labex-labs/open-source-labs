# Definir una función para obtener los promedios iniciales

A continuación, definiremos una función `get_initial_means` que toma los datos de muestra, el método de inicialización y el estado aleatorio como entradas y devuelve los promedios de inicialización.

```python
def get_initial_means(X, init_params, r):
    # Run a GaussianMixture with max_iter=0 to output the initialization means
    gmm = GaussianMixture(
        n_components=4, init_params=init_params, tol=1e-9, max_iter=0, random_state=r
    ).fit(X)
    return gmm.means_
```
