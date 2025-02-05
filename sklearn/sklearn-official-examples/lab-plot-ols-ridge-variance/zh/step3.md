# 定义分类器

在这一步中，我们将定义普通最小二乘法（OLS）和岭回归分类器。

```python
classifiers = dict(
    ols=linear_model.LinearRegression(), ridge=linear_model.Ridge(alpha=0.1)
)
```
