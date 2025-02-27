# Definir clasificadores

En este paso, definiremos los clasificadores de Mínimos Cuadrados Ordinarios (OLS) y Regresión Ridge.

```python
classifiers = dict(
    ols=linear_model.LinearRegression(), ridge=linear_model.Ridge(alpha=0.1)
)
```
