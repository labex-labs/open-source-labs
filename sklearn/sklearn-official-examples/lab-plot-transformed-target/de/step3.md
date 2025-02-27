# Trainieren und Auswerten eines linearen Regressionsmodells auf den ursprünglichen Zielwerten

Wir trainieren und evaluieren ein lineares Regressionsmodell auf den ursprünglichen Zielwerten. Aufgrund der Nichtlinearität wird das trainierte Modell bei der Vorhersage nicht präzise sein.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("Lineare Regression auf ursprüngliche Zielwerte:")
for key, val in score.items():
    print(f"{key}: {val}")
```
