# Fit a Model Without Constraints

We will fit a model on the generated data without any constraints to see how the model performs without any restrictions.

```python
gbdt_no_cst = HistGradientBoostingRegressor()
gbdt_no_cst.fit(X, y)
```


