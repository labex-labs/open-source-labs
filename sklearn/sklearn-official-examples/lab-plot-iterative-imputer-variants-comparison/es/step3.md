# Agregar valores faltantes

Agregaremos un solo valor faltante a cada fila del conjunto de datos.

```python
X_missing = X_full.copy()
y_missing = y_full
missing_samples = np.arange(n_samples)
missing_features = rng.choice(n_features, n_samples, replace=True)
X_missing[missing_samples, missing_features] = np.nan
```
