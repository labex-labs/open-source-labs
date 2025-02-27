# Определение классификаторов

В этом шаге мы определим классификаторы OLS и Ridge Regression.

```python
classifiers = dict(
    ols=linear_model.LinearRegression(), ridge=linear_model.Ridge(alpha=0.1)
)
```
