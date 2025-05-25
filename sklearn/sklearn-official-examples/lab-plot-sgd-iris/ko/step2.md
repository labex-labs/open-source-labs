# 모델 학습

이제 `fit()` 메서드를 사용하여 iris 데이터셋에 대한 SGDClassifier 모델을 학습합니다. 이 메서드는 입력 데이터와 대상 값을 입력으로 받아 주어진 데이터로 모델을 학습시킵니다.

```python
clf = SGDClassifier(alpha=0.001, max_iter=100).fit(X, y)
```
