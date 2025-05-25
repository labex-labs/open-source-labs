# 원 데이터로 Ridge 회귀 모델 학습

이 섹션에서는 인코딩 여부와 구간 교차 검증 (interval cross-validation) 유무에 따라 타겟 인코더를 사용하여 데이터셋에 Ridge 회귀 모델을 학습하고 그 영향을 살펴봅니다. 먼저, 원본 특징으로 Ridge 모델을 학습합니다. 다음 코드를 실행하여 Ridge 모델을 학습합니다.

```python
ridge = Ridge(alpha=1e-6, solver="lsqr", fit_intercept=False)

raw_model = ridge.fit(X_train, y_train)
print("Raw Model score on training set: ", raw_model.score(X_train, y_train))
print("Raw Model score on test set: ", raw_model.score(X_test, y_test))
```
