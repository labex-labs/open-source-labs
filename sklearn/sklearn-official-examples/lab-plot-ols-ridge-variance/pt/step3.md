# Definir Classificadores

Neste passo, definiremos os classificadores de Regressão Linear (OLS) e Regressão Ridge.

```python
classifiers = dict(
    ols=linear_model.LinearRegression(), ridge=linear_model.Ridge(alpha=0.1)
)
```
