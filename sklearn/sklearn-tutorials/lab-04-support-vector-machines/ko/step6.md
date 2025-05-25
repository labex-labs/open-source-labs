# 밀도 추정 및 신규성 탐지

- SVM 은 `OneClassSVM` 클래스를 사용하여 밀도 추정 및 신규성 탐지에도 활용될 수 있습니다.

```python
clf = svm.OneClassSVM()
clf.fit(X)
clf.predict(X)
```
