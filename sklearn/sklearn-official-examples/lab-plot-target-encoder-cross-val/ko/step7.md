# 교차 검증 없이 Ridge 회귀 모델 학습

`TargetEncoder.fit_transform`은 구간 교차 검증을 사용하지만, `TargetEncoder.transform` 자체는 교차 검증을 수행하지 않습니다. 범주형 특징을 변환하기 위해 전체 학습 데이터 집합의 집계를 사용합니다. 따라서 교차 검증을 비활성화하려면 `TargetEncoder.fit`을 먼저 실행하고 `TargetEncoder.transform`을 사용할 수 있습니다. 이렇게 인코딩된 데이터는 Ridge 모델에 전달됩니다. 교차 검증 없이 Ridge 모델을 학습하는 코드는 다음과 같습니다.

```python
target_encoder = TargetEncoder(random_state=0)
target_encoder.fit(X_train, y_train)
X_train_no_cv_encoding = target_encoder.transform(X_train)
X_test_no_cv_encoding = target_encoder.transform(X_test)

model_no_cv = ridge.fit(X_train_no_cv_encoding, y_train)
print(
    "Model without CV on training set: ",
    model_no_cv.score(X_train_no_cv_encoding, y_train),
)
print(
    "Model without CV on test set: ", model_no_cv.score(X_test_no_cv_encoding, y_test)
)
```
