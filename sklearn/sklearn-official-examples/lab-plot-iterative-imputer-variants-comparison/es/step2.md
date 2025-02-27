# Cargar el conjunto de datos

Cargaremos el conjunto de datos de viviendas de California de Scikit-Learn. Solo usaremos 2k muestras para reducir el tiempo de cómputo.

```python
N_SPLITS = 5

rng = np.random.RandomState(0)

X_full, y_full = fetch_california_housing(return_X_y=True)
X_full = X_full[::10]
y_full = y_full[::10]
n_samples, n_features = X_full.shape
```
