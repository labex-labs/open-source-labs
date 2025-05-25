# 모델 학습

두 개의 SVM 모델을 생성합니다. 첫 번째 모델은 샘플 가중치를 고려하지 않고, 두 번째 모델은 방금 생성한 샘플 가중치를 고려합니다.

```python
clf_no_weights = svm.SVC(gamma=1)
clf_no_weights.fit(X, y)

clf_weights = svm.SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=sample_weight_last_ten)
```
