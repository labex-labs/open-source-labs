# Entraînez et évaluez un modèle de régression linéaire sur les cibles transformées pour les données sur le logement d'Ames

Nous entraînons et évaluons un modèle de régression linéaire sur les cibles transformées en utilisant TransformedTargetRegressor pour les données sur le logement d'Ames.

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

print("\nRégression linéaire sur les cibles transformées:")
for key, val in score.items():
    print(f"{key}: {val}")
```
