# Generar un conjunto de datos sintético

Generamos un conjunto de datos sintético en el que `X` e `y` están relacionados linealmente. Diez de las características de `X` se utilizarán para generar `y`. Las otras características no son útiles para predecir `y`. Además, generamos un conjunto de datos donde `n_samples == n_features`. Esta configuración es desafiante para un modelo OLS y puede conducir a pesos arbitrariamente grandes. Tener una prioridad sobre los pesos y una penalización alivia el problema. Finalmente, se agrega ruido gaussiano.

```python
from sklearn.datasets import make_regression

X, y, true_weights = make_regression(
    n_samples=100,
    n_features=100,
    n_informative=10,
    noise=8,
    coef=True,
    random_state=42,
)
```
