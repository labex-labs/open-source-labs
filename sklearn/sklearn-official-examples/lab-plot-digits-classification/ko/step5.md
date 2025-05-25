# 서포트 벡터 머신 학습

`sklearn`의 `svm.SVC()` 메서드를 사용하여 훈련 샘플에 대한 서포트 벡터 분류기를 학습합니다.

```python
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)
```
