# Entraînez et évaluez un modèle de régression linéaire sur les cibles transformées

Nous entraînons et évaluons un modèle de régression linéaire sur les cibles transformées en utilisant TransformedTargetRegressor. La fonction logarithmique linearise les cibles, permettant une meilleure prédiction même avec un modèle linéaire similaire, comme le montre l'erreur absolue médiane (MedAE).

```python
ridge_cv_with_trans_target = TransformedTargetRegressor(
    regressor=RidgeCV(), func=np.log1p, inverse_func=np.expm1
).fit(X_train, y_train)
y_pred_ridge_with_trans_target = ridge_cv_with_trans_target.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge_with_trans_target):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge_with_trans_target):.3f}",
}

print("\nRégression linéaire sur les cibles transformées:")
for key, val in score.items():
    print(f"{key}: {val}")
```
