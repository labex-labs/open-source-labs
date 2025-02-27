# Обучите и оцените модель линейной регрессии на преобразованных целевых переменных для данных о недвижимости в Амесе

Мы обучаем и оцениваем модель линейной регрессии на преобразованных целевых переменных с использованием TransformedTargetRegressor для данных о недвижимости в Амесе.

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

print("\nЛинейная регрессия на преобразованных целевых переменных:")
for key, val in score.items():
    print(f"{key}: {val}")
```
