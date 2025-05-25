# Treinar e avaliar um modelo de regressão linear nos alvos transformados para dados de habitação de Ames

Treinamos e avaliamos um modelo de regressão linear nos alvos transformados usando `TransformedTargetRegressor` para os dados de habitação de Ames.

```python
ridge_cv_with_trans_target = TransformedTargetRegressor(
    regressor=RidgeCV(),
    transformer=QuantileTransformer(n_quantiles=900, output_distribution="normal"),
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
