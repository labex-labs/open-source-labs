# Treinar e avaliar um modelo de regressão linear nos alvos originais para dados de habitação de Ames

Treinamos e avaliamos um modelo de regressão linear nos alvos originais para os dados de habitação de Ames.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("\nRegressão Linear nos alvos originais:")
for key, val in score.items():
    print(f"{key}: {val}")
```
