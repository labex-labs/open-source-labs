# Cargar el conjunto de datos

Utilizaremos la función `make_gaussian_quantiles` de `sklearn.datasets` para generar un conjunto de datos. Esta función genera Gaussianas isotrópicas y agrega separación entre las clases para hacer el problema más difícil.

```python
X, y = make_gaussian_quantiles(
    n_samples=13000, n_features=10, n_classes=3, random_state=1
)
```
