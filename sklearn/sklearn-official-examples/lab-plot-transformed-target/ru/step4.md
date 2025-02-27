# Обучите и оцените модель линейной регрессии на преобразованных целевых переменных

Мы обучаем и оцениваем модель линейной регрессии на преобразованных целевых переменных с использованием TransformedTargetRegressor. Логарифмическая функция линейно преобразует целевые переменные, что позволяет получить более точные предсказания, даже при использовании похожей линейной модели, как показывает медианная абсолютная ошибка (MedAE).

```python
ridge_cv_with_trans_target = TransformedTargetRegressor(
    regressor=RidgeCV(), func=np.log1p, inverse_func=np.expm1
).fit(X_train, y_train)
y_pred_ridge_with_trans_target = ridge_cv_with_trans_target.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge_with_trans_target):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge_with_trans_target):.3f}",
}

print("\nЛинейная регрессия на преобразованных целевых переменных:")
for key, val in score.items():
    print(f"{key}: {val}")
```
