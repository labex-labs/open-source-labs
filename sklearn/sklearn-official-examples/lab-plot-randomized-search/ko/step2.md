# SVM 모델 생성

SGD 훈련을 사용하는 선형 SVM 모델을 생성합니다.

```python
# SGD 훈련을 사용하는 SVM 모델 생성
clf = SGDClassifier(loss="hinge", penalty="elasticnet", fit_intercept=True)
```
