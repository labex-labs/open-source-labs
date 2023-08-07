# Fit a Model With Monotonic Constraints

We will now fit another model on the same data but with monotonic constraints on the features. We will impose a monotonic increase constraint on the first feature and a monotonic decrease constraint on the second feature.

```python
gbdt_with_monotonic_cst = HistGradientBoostingRegressor(monotonic_cst=[1, -1])
gbdt_with_monotonic_cst.fit(X, y)
```
