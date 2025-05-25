# Treinar e avaliar um modelo de regressão linear nos alvos transformados

Treinamos e avaliamos um modelo de regressão linear nos alvos transformados usando `TransformedTargetRegressor`. A função logarítmica lineariza os alvos, permitindo uma melhor previsão mesmo com um modelo linear semelhante, conforme demonstrado pelo erro absoluto mediano (MedAE).

```python
ridge_cv_with_trans_target = TransformedTargetRegressor(
    regressor=RidgeCV(), func=np.log1p, inverse_func=np.expm1
).fit(X_train, y_train)
y_pred_ridge_with_trans_target = ridge_cv_with_trans_target.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge_with_trans_target):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge_with_trans_target):.3f}",
}

print("\nRegressão Linear nos alvos transformados:")
for key, val in score.items():
    print(f"{key}: {val}")
```
