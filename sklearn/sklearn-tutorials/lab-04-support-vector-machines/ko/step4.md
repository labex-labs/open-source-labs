# 불균형 문제

- SVM 은 `class_weight` 매개변수를 조정하여 불균형 문제를 처리할 수 있습니다.

```python
clf = svm.SVC(class_weight={1: 10})
clf.fit(X, y)
```
