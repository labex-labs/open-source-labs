# Entrenar y evaluar un modelo de regresión lineal en los objetivos originales

Entrenamos y evaluamos un modelo de regresión lineal en los objetivos originales. Debido a la no linealidad, el modelo entrenado no será preciso durante la predicción.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("Linear Regression on original targets:")
for key, val in score.items():
    print(f"{key}: {val}")
```
