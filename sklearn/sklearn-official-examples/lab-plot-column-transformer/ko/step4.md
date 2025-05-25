# 학습 및 테스트

훈련 데이터에 파이프라인을 적용하고, 이를 사용하여 `X_test`에 대한 주제를 예측할 것입니다. 그런 다음 파이프라인의 성능 지표를 출력합니다.

```python
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("분류 보고서:\n\n{}".format(classification_report(y_test, y_pred)))
```
