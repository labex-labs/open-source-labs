# Train and evaluate a linear regression model on the transformed targets

We train and evaluate a linear regression model on the transformed targets using TransformedTargetRegressor. The logarithmic function linearizes the targets, allowing better prediction even with a similar linear model as reported by the median absolute error (MedAE).

```python
ridge_cv_with_trans_target = TransformedTargetRegressor(
    regressor=RidgeCV(), func=np.log1p, inverse_func=np.expm1
).fit(X_train, y_train)
y_pred_ridge_with_trans_target = ridge_cv_with_trans_target.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge_with_trans_target):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge_with_trans_target):.3f}",
}

print("\nLinear Regression on transformed targets:")
for key, val in score.items():
    print(f"{key}: {val}")
```
