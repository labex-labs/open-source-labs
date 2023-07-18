# Define Classifiers

In this step, we will define the OLS and Ridge Regression classifiers.

```python
classifiers = dict(
    ols=linear_model.LinearRegression(), ridge=linear_model.Ridge(alpha=0.1)
)
```
