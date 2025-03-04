# Trainieren und Auswerten eines linearen Regressionsmodells auf den transformierten Zielwerten für die Ames Wohnungsdaten

Wir trainieren und evaluieren ein lineares Regressionsmodell auf den transformierten Zielwerten mit Hilfe von TransformedTargetRegressor für die Ames Wohnungsdaten.

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

print("\nLineare Regression auf transformierte Zielwerte:")
for key, val in score.items():
    print(f"{key}: {val}")
```
