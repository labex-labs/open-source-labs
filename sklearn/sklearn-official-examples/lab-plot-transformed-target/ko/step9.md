# Ames 주택 데이터의 변환된 타겟에 대한 선형 회귀 모델 학습 및 평가

Ames 주택 데이터의 변환된 타겟에 대해 TransformedTargetRegressor 를 사용하여 선형 회귀 모델을 학습하고 평가합니다.

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

print("\n변환된 타겟에 대한 선형 회귀:")
for key, val in score.items():
    print(f"{key}: {val}")
```
