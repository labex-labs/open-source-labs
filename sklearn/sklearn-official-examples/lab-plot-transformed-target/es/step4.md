# Entrenar y evaluar un modelo de regresión lineal en los objetivos transformados

Entrenamos y evaluamos un modelo de regresión lineal en los objetivos transformados usando TransformedTargetRegressor. La función logarítmica lineariza los objetivos, lo que permite una mejor predicción incluso con un modelo lineal similar, como lo indica el error absoluto mediano (MedAE).

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
