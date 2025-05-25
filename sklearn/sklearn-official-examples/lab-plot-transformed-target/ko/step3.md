# 원본 대상에 대한 선형 회귀 모델 학습 및 평가

원본 대상에 대한 선형 회귀 모델을 학습하고 평가합니다. 비선형성으로 인해 학습된 모델은 예측 시 정확하지 않습니다.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("원본 대상에 대한 선형 회귀:")
for key, val in score.items():
    print(f"{key}: {val}")
```
