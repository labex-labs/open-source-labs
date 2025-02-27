# Trainieren und Auswerten eines linearen Regressionsmodells auf den transformierten Zielwerten

Wir trainieren und evaluieren ein lineares Regressionsmodell auf den transformierten Zielwerten mithilfe von TransformedTargetRegressor. Die logarithmische Funktion linearisiert die Zielwerte, was eine bessere Vorhersage ermöglicht, auch mit einem ähnlichen linearen Modell, wie dies durch den median absolute error (MedAE) berichtet wird.

```python
ridge_cv_with_trans_target = TransformedTargetRegressor(
    regressor=RidgeCV(), func=np.log1p, inverse_func=np.expm1
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
