# Обучите и оцените модель линейной регрессии на исходных целевых переменных для данных о недвижимости в Амесе

Мы обучаем и оцениваем модель линейной регрессии на исходных целевых переменных для данных о недвижимости в Амесе.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("\nЛинейная регрессия на исходных целевых переменных:")
for key, val in score.items():
    print(f"{key}: {val}")
```
