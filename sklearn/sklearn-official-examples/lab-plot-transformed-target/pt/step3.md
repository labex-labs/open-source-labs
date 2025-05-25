# Treinar e avaliar um modelo de regressão linear nos alvos originais

Treinamos e avaliamos um modelo de regressão linear nos alvos originais. Devido à não-linearidade, o modelo treinado não será preciso durante a previsão.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("Regressão Linear nos alvos originais:")
for key, val in score.items():
    print(f"{key}: {val}")
```
