# Unbalanced Problems

- SVMs can handle unbalanced problems by adjusting the `class_weight` parameter:

```python
clf = svm.SVC(class_weight={1: 10})
clf.fit(X, y)
```
