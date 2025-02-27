# Entraînez et évaluez un modèle de régression linéaire sur les cibles originales pour les données sur le logement d'Ames

Nous entraînons et évaluons un modèle de régression linéaire sur les cibles originales pour les données sur le logement d'Ames.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("\nRégression linéaire sur les cibles originales:")
for key, val in score.items():
    print(f"{key}: {val}")
```
