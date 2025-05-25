# 교차 검증을 사용한 Ridge 회귀 모델 학습

다음으로 `TargetEncoder`와 Ridge 모델을 포함하는 파이프라인을 생성합니다. 이 파이프라인은 교차 검증을 사용하는 `TargetEncoder.fit_transform`을 사용합니다. 교차 검증을 사용하여 Ridge 모델을 학습하는 코드는 다음과 같습니다.

```python
model_with_cv = make_pipeline(TargetEncoder(random_state=0), ridge)
model_with_cv.fit(X_train, y_train)
print("Model with CV on training set: ", model_with_cv.score(X_train, y_train))
print("Model with CV on test set: ", model_with_cv.score(X_test, y_test))
```
