# Generar datos

En este paso, generamos un conjunto de datos aleatorios con `n_samples` muestras y `n_features` características. También agregamos algunos valores atípicos al conjunto de datos.

```python
n_samples = 80
n_features = 5

# Generar conjunto de datos aleatorio
rng = np.random.RandomState(42)
X = rng.randn(n_samples, n_features)

# Agregar valores atípicos al conjunto de datos
n_outliers = 20
outliers_index = rng.permutation(n_samples)[:n_outliers]
outliers_offset = 10.0 * (
    np.random.randint(2, size=(n_outliers, n_features)) - 0.5
)
X[outliers_index] += outliers_offset
```
