# Klassifizierer definieren

In diesem Schritt werden wir den OLS- und den Ridge-Regression-Klassifizierer definieren.

```python
classifiers = dict(
    ols=linear_model.LinearRegression(), ridge=linear_model.Ridge(alpha=0.1)
)
```
