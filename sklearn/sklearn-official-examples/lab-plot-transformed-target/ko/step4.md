# 변환된 대상에 대한 선형 회귀 모델 학습 및 평가

TransformedTargetRegressor 를 사용하여 변환된 대상에 대한 선형 회귀 모델을 학습하고 평가합니다. 로그 함수는 대상을 선형화하여, 중앙 절대 오차 (MedAE) 와 같은 선형 모델로도 더 나은 예측을 가능하게 합니다.

```python
ridge_cv_with_trans_target = TransformedTargetRegressor(
    regressor=RidgeCV(), func=np.log1p, inverse_func=np.expm1
).fit(X_train, y_train)
y_pred_ridge_with_trans_target = ridge_cv_with_trans_target.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge_with_trans_target):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge_with_trans_target):.3f}",
}

print("\n변환된 대상에 대한 선형 회귀:")
for key, val in score.items():
    print(f"{key}: {val}")
```
