# Generar datos aleatorios

Generaremos datos aleatorios con la función `make_regression` de scikit-learn. Estableceremos `n_samples` en 10, `n_features` en 10 y `random_state` en 1. Esta función devolverá nuestras características de entrada X, nuestra variable objetivo y, y los valores reales de los coeficientes w.

```python
X, y, w = make_regression(
    n_samples=10, n_features=10, coef=True, random_state=1, bias=3.5
)
```
