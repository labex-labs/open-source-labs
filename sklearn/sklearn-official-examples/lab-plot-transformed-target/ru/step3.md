# Обучите и оцените модель линейной регрессии на исходных целевых переменных

Мы обучаем и оцениваем модель линейной регрессии на исходных целевых переменных. В силу нелинейности, модель, обученная на этих данных, будет менее точной при предсказании.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("Линейная регрессия на исходных целевых переменных:")
for key, val in score.items():
    print(f"{key}: {val}")
```
