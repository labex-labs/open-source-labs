# 모델 평가

MLPClassifier 의 정확도를 학습 데이터셋과 테스트 데이터셋에서 계산하여 평가합니다.

```python
print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))
```
