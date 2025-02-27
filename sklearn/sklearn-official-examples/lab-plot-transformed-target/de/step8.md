# Trainieren und Auswerten eines linearen Regressionsmodells auf den ursprünglichen Zielwerten für die Ames Wohnungsdaten

Wir trainieren und evaluieren ein lineares Regressionsmodell auf den ursprünglichen Zielwerten für die Ames Wohnungsdaten.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("\nLineare Regression auf ursprüngliche Zielwerte:")
for key, val in score.items():
    print(f"{key}: {val}")
```
